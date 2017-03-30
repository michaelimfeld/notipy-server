"""
`notipyserver` - User-Notification-Framework server

Provides test cases for the notipyserver recipients module.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
from mock import patch

from notipyserver.handlers.notifications import send_post
from notipyserver.errors import NotipyError


def test_notifications_post():
    """
    Test notifications post
    """
    request = "notipyserver.handlers.notifications.request"
    dispatch = "notipyserver.handlers.notifications.dispatch_notification"
    response = "notipyserver.handlers.notifications.create_response"

    with patch(request) as mock, patch(dispatch), \
            patch(response) as response_mock:

        mock.json = {"backend": 1, "recipient": "foouser", "message": "foobar"}

        send_post()
        response_mock.assert_called_with(200, "success")


def test_notifications_post_missing():
    """
    Test notifications post if a param is missing
    """
    request = "notipyserver.handlers.notifications.request"
    dispatch = "notipyserver.handlers.notifications.dispatch_notification"
    response = "notipyserver.handlers.notifications.create_response"

    with patch(request) as mock, patch(dispatch), \
            patch(response) as response_mock:

        mock.json = {"backend": 1, "message": "foobar"}

        send_post()
        response_mock.assert_called_with(
            400, "error", "One of the following parameters is missing:"
            " backend, recipient, message.")


def test_notifications_post_empty():
    """
    Test notifications post if a param is empty
    """
    request = "notipyserver.handlers.notifications.request"
    dispatch = "notipyserver.handlers.notifications.dispatch_notification"
    response = "notipyserver.handlers.notifications.create_response"

    with patch(request) as mock, patch(dispatch), \
            patch(response) as response_mock:

        mock.json = {"backend": 1, "message": "foobar", "recipient": ""}

        send_post()
        response_mock.assert_called_with(
            400, "error", "One of the following parameters is undefined:"
            " backend, recipient, message.")


def test_notifications_post_error1():
    """
    Test notifications post if a known NotipyError occurs
    """
    request = "notipyserver.handlers.notifications.request"
    dispatch = "notipyserver.handlers.notifications.dispatch_notification"
    response = "notipyserver.handlers.notifications.create_response"

    with patch(request) as mock, patch(dispatch) as dispatch_mock, \
            patch(response) as response_mock:

        dispatch_mock.side_effect = NotipyError("Custom error ocurred")
        mock.json = {"backend": 1, "recipient": "foouser", "message": "foobar"}

        send_post()
        response_mock.assert_called_with(500, "error", "Custom error ocurred")


def test_notifications_post_error2():
    """
    Test notifications post if a unknown error occurs
    """
    request = "notipyserver.handlers.notifications.request"
    dispatch = "notipyserver.handlers.notifications.dispatch_notification"
    response = "notipyserver.handlers.notifications.create_response"

    with patch(request) as mock, patch(dispatch) as dispatch_mock, \
            patch(response) as response_mock:

        dispatch_mock.side_effect = ValueError()
        mock.json = {"backend": 1, "recipient": "foouser", "message": "foobar"}

        send_post()
        response_mock.assert_called_with(500, "error",
                                         "An unknown error occurred.")
