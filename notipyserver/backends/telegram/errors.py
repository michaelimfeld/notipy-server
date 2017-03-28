"""
`notipyserver` - User-Notification-Framework server

Provides a collection of all possible
notipy-telegram errors.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
from notipyserver.errors import NotipyError


class UserNotRegisteredError(NotipyError):
    """
    Exception which is raised if the user could not
    be found in the users file.
    """
    pass


class GroupNotRegisteredError(NotipyError):
    """
    Exception which is raised if the user could not
    be found in the users file.
    """
    pass


class TelegramConfigurationError(NotipyError):
    """
    Exception which is raised if telegram is not
    properly configured on the system.
    """
    pass
