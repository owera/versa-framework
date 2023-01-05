# SPDX-License-Identifier: MIT
"""Module to allow for backwards compatibility for existing code and extensions."""

from versa import *

__title__ = "versa framework"
__author__ = "Versa Developers"
__license__ = "MIT"
__copyright__ = "Copyright 022-present Versa Developers"
__version__ = "2.4.0a"

__path__ = __import__("pkgutil").extend_path(__path__, __name__)
