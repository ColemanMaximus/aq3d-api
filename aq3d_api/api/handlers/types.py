from enum import Enum

from aq3d_api.api.handlers.server import get_servers
from aq3d_api.api.handlers.item import get_items
from aq3d_api.api.handlers.map import get_maps
from aq3d_api.api.handlers.dialog import get_dialogs

class Handlers(Enum):
    SERVERS = get_servers
    ITEMS = get_items
    MAPS = get_maps
    DIALOGS = get_dialogs
