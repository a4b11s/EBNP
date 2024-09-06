"""
:author: Artem Bazyl
:license: MIT
"""

from .modules import event
from .enums import args_type, methods

from .modules.event import Event
from .enums.args_type import TYPES_ENUM
from .enums.methods import Methods


__author__ = "Artem Bazyl"
__license__ = "MIT"
__version__ = "0.0.1"
__all__ = ["event", "args_type", "Event", "TYPES_ENUM", "methods", "Methods"]
