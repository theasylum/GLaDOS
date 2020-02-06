from typing import Union

from .route_type import BOT_ROUTES, RouteType
from .utils import PyJSON


class SlackVerification:
    """An object to hold slack verification data

    Parameters
    ----------
    data: str
        raw request body. This is used to verify the message is from slack.
    timestamp: str
        The X-Slack-Request-Timestamp from the headers of the request. This is used to verify the message is from slack.
    signature: str
        The X-Slack-Signature from the headers of the request. This is used to verify the message is from slack.
    """

    def __init__(self, data: str, timestamp: str = None, signature: str = None):
        self.data = data
        self.timestamp = timestamp
        self.signature = signature

    @property
    def json(self) -> dict:
        return {
            "data": self.data,
            "timestamp": self.timestamp,
            "signature": self.signature,
        }


class GladosRequest:
    """GLaDOS Request Object. This holds all the data required to process the request.

    Parameters
    ----------
    route_type: RouteType
        what type of route is this
    route: str
        what is the route to be called
    slack_verify: SlackVerification
        slack data used for verifying the request came from Slack
    bot_name: str
        The name of the bot to send the request to. This is used for select RouteTypes
    json:
        the json paylod of the request
    kwargs

    Examples
    --------
    >>> request = GladosRequest(RouteType.SendMessage, "send_mock", json={"message":"my message"})
    >>> print(request.json.message)
    my message
    >>> try:
    ...    print(request.json.other_param)
    ... except AttributeError:
    ...     print("ERROR")
    ERROR
    """

    def __init__(
        self,
        route_type: RouteType,
        route: str = None,
        slack_verify: SlackVerification = None,
        bot_name: str = None,
        json: Union[str, dict] = None,
        **kwargs,
    ):

        if not json:
            json = dict()

        self.json = PyJSON(json)
        self.route_type = route_type
        self.bot_name = bot_name
        self._route = route
        self.slack_verify = slack_verify
        self.response_url = None
        self.trigger_id = None

        if route_type is RouteType.Interaction:
            self.response_url = self.json.get("response_url")
            self.trigger_id = self.json.get("trigger_id")

        if route_type is RouteType.Menu:
            self._route = self.json.action_id

        if route_type is RouteType.Interaction:
            self._route = self.json.actions[0].action_id

        if route_type is RouteType.Events:
            self._route = self.json.event.type

    @property
    def route(self) -> str:
        """the actual route

        If the route automatically prefixed the route with the bot name, it will return the route with the prefix
        """

        return (
            f"{self.bot_name}_{self._route}"
            if self.route_type in BOT_ROUTES
            else self._route
        )

    @route.setter
    def route(self, value):
        self._route = value
