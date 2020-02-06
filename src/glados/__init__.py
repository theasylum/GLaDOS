import logging

from .bot import BotImporter, GladosBot
from .configs import GladosConfig, read_config
from .core import Glados
from .errors import (
    GladosBotNotFoundError,
    GladosError,
    GladosPathExistsError,
    GladosRouteNotFoundError,
)
from .plugin import GladosPlugin, PluginImporter
from .request import GladosRequest, SlackVerification
from .route_type import BOT_ROUTES, VERIFY_ROUTES, EventRoutes, RouteType
from .router import GladosRoute, GladosRouter
from .utils import PyJSON, get_enc_var, get_var

# LOGGING_FORMAT = "%(asctime)s :: %(levelname)-8s :: [%(filename)s:%(lineno)s :: %(funcName)s() ] %(message)s"
LOGGING_FORMAT = (
    "%(levelname)-8s :: [%(filename)s:%(lineno)s :: %(funcName)s() ] %(message)s"
)
logging.basicConfig(
    level=logging.DEBUG, format=LOGGING_FORMAT, datefmt="%Y-%m-%d %H:%M:%S"
)


__all__ = [
    "Glados",
    "GladosBot",
    "GladosRequest",
    "RouteType",
    "EventRoutes",
    "GladosPlugin",
    "GladosConfig",
    "read_config",
]
