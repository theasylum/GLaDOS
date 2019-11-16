from enum import Enum


class RouteType(Enum):
    SendMessage = 1
    Response = 2
    Callback = 3
    Slash = 4
    Events = 5
    Interaction = 6
    Menu = 7


BOT_ROUTES = [RouteType.Events, RouteType.Interaction]
VERIFY_ROUTES = [
    RouteType.Slash,
    RouteType.Events,
    RouteType.Interaction,
    RouteType.Menu,
]


class EventRoutes(Enum):
    app_home_opened = 1
    message = 2
