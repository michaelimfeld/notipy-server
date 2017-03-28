"""
`notipyserver` - User-Notification-Framework server

Provides functions to send notification messages over
several backends.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
from .backendtype import BackendType
from .errors import BackendNotFoundError
from .backends.telegram.messagehandler import send as telegram_handler
from .backends.telegram.messagehandler import send_to_group \
        as telegram_group_handler


def dispatch_notification(backend, recipient, message):
    """
    Dispatches a notification message to a backend.

    Args:
        backend (int): The backend_type to be used.
        recipient (str): The recipient of the message.
        message (str): The message to be sent.

    Raises:
        BackendNotFoundError: If the given backend could not be found.
    """
    handlers = {BackendType.TELEGRAM.value: telegram_handler,
                BackendType.TELEGRAMGROUP.value: telegram_group_handler}

    handler = handlers.get(backend)
    if not handler:
        raise BackendNotFoundError("Backend with id '{}' could not be found."
                                   .format(backend))

    handler(recipient, message)
