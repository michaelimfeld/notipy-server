"""
`notipyserver` - User-Notification-Framework server

Provides the request handler for recipients.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
from flask import request

from notipyserver.app import app
from notipyserver.recipientsmanager import get_recipients
from notipyserver.response import create_response
from notipyserver.errors import NotipyError


@app.route("/api/v1/recipients", methods=["GET"])
def recipients_get():
    """
    Recipients
    The Recipients endpoint returns all registered recipients for
    a given backend.
    :param backend: Backend type.
    :type backend: int

    :rtype: Response
    """
    backend = request.args.get("backend")
    if not backend:
        return create_response(400, "error", "Backend parameter is missing.")

    try:
        recipients = get_recipients(int(backend))
        return create_response(200, "success", "", recipients)
    except NotipyError as exc:
        return create_response(500, "error", str(exc))
    # To prevent crashes, it is required to catch all exceptions
    except Exception as exc:  # pylint: disable=broad-except
        return create_response(500, "error", "An unknown error occurred.")
