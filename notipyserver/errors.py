"""
`notipyserver` - User-Notification-Framework server

Provides the base exception for all
notipy specific errors.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""


class NotipyError(Exception):
    """
    Represents the base exception for notipy specific
    errors.
    """
    pass


class BackendNotFoundError(NotipyError):
    """
    Exception which is raised if the backend could
    not be found.
    """
    pass


class NoConfigurationError(NotipyError):
    """
    Exception which is raised if the notipy configuration
    file does not exist.
    """
    pass
