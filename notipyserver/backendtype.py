"""
`notipyserver` - User-Notification-Framework server

Provides the notipy BackendType enum.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
from enum import Enum


class BackendType(Enum):
    """
    Provides the backend types.
    """
    TELEGRAM = 1
    TELEGRAMGROUP = 2
