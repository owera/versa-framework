"""
versacord Framework
~~~~~~~~~~~~~~~~~~~

Imagine a framework...

:copyright: (c) 2022-present versacord Framework Developers
:license: MIT, see LICENSE for more details.
"""

__title__ = "versacord framework"
__author__ = "versacord Developers"
__license__ = "MIT"
__copyright__ = "Copyright 2022-present versacord Developers"
__version__ = "1.0.0"

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

import logging
from typing import Literal, NamedTuple

from . import abc, opus, ui, utils
from .activity import *
from .appinfo import *
from .application_command import *
from .asset import *
from .audit_logs import *
from .auto_moderation import *
from .bans import *
from .channel import *
from .client import *
from .colour import *
from .components import *
from .embeds import *
from .emoji import *
from .enums import *
from .errors import *
from .file import *
from .flags import *
from .guild import *
from .health_check import *
from .integrations import *
from .interactions import *
from .invite import *
from .member import *
from .mentions import *
from .message import *
from .object import *
from .partial_emoji import *
from .permissions import *
from .player import *
from .raw_models import *
from .reaction import *
from .role import *
from .scheduled_events import *
from .shard import *
from .stage_instance import *
from .sticker import *
from .team import *
from .template import *
from .threads import *
from .user import *
from .voice_client import *
from .webhook import *
from .widget import *


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(major=2, minor=4, micro=0, releaselevel="alpha", serial=0)

logging.getLogger(__name__).addHandler(logging.NullHandler())
