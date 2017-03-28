"""
`notipyserver` - User-Notification-Framework server

Provides functions to get information about registered
recipients.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
from .backendtype import BackendType
from .errors import BackendNotFoundError
from .backends.telegram.usermanager import get_users as telegram_handler
from .backends.telegram.usermanager import get_groups as telegram_group_handler


def get_recipients(backend):
    """
    Gets all recipients for given backend.

    Args:
        backend (int): The backend_type to be used.

    Returns:
        list: List of recipients.
    """
    handlers = {BackendType.TELEGRAM.value: telegram_handler,
                BackendType.TELEGRAMGROUP.value: telegram_group_handler}

    handler = handlers.get(backend)
    if not handler:
        raise BackendNotFoundError("Backend with id '{}' could not be found."
                                   .format(backend))

    return handler()
