"""
`notipyserver` - User-Notification-Framework server

Provides the generic response function
for all web requests.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
import json
from flask import make_response


def create_response(return_code, status, message=str(), data=None):
    """
    Creates a flask response with given attributes.
    This function is used by all web requests in order to
    create consistent and generic repsonses.

    Args:
        return_code (int): The http status/return code.
        status (str): The status of the response, (e.g. success, error).
        message (str): Message which gives information about the response
            or sent request.
        data (dict): The data to be sent.

    Returns:
        The flask response object.
    """
    response_content = {"status": status, "message": message, "data": data}
    return make_response(json.dumps(response_content), return_code)
