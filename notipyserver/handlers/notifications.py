"""
`notipyserver` - User-Notification-Framework server

Provides the request handler for notifications.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
from flask import request

from notipyserver.app import app
from notipyserver.notificationmanager import dispatch_notification
from notipyserver.response import create_response
from notipyserver.errors import NotipyError


@app.route("/api/v1/notifications/send", methods=["POST"])
def send_post():
    """
    Sends a notification message.
    Sends a notification with given message to given
    recipient over given backend.

    :param Notification: The Notification object.
    :type Notification: dict | bytes
    """
    params = request.json
    backend_type = params.get("backend")
    recipient = params.get("recipient")
    message = params.get("message")

    if not backend_type or not recipient or not message:
        return create_response(400, "error",
                               "One of the following parameters is missing:"
                               " backend, recipient, message.")

    try:
        dispatch_notification(backend_type, recipient, message)
    except NotipyError as exc:
        return create_response(500, "error", str(exc))
    # To prevent crashes, it is required to catch all exceptions
    except Exception as exc:  # pylint: disable=broad-except
        return create_response(500, "error", "An unknown error occurred.")

    return create_response(200, "success")
