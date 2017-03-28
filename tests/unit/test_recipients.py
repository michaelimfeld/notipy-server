"""
`notipyserver` - User-Notification-Framework server

Provides test cases for the notipyserver recipients module.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
from mock import patch

from notipyserver.handlers.recipients import recipients_get
from notipyserver.errors import NotipyError


def test_recipients_get():
    """
    Test recipients get
    """
    request = "notipyserver.handlers.recipients.request"
    get_rec = "notipyserver.handlers.recipients.get_recipients"
    response = "notipyserver.handlers.recipients.create_response"

    with patch(request) as mock, patch(get_rec) as recipients_mock, \
            patch(response) as response_mock:

        recipients_mock.return_value = ["foouser"]
        mock.args = {"backend": 1}

        recipients_get()
        response_mock.assert_called_with(200, "success", "", ["foouser"])


def test_recipients_get_parammiss():
    """
    Test recipients get if backend parameter is missing
    """
    request = "notipyserver.handlers.recipients.request"
    get_rec = "notipyserver.handlers.recipients.get_recipients"
    response = "notipyserver.handlers.recipients.create_response"

    with patch(request) as mock, patch(get_rec) as recipients_mock, \
            patch(response) as response_mock:

        recipients_mock.return_value = ["foouser"]
        mock.args = {}

        recipients_get()
        response_mock.assert_called_with(400, "error",
                                         "Backend parameter is missing.")


def test_recipients_get_error1():
    """
    Test recipients get if a known NotipyError occurs
    """
    request = "notipyserver.handlers.recipients.request"
    get_rec = "notipyserver.handlers.recipients.get_recipients"
    response = "notipyserver.handlers.recipients.create_response"

    with patch(request) as mock, patch(get_rec) as recipients_mock, \
            patch(response) as response_mock:

        recipients_mock.side_effect = NotipyError("Custom error occurred.")

        recipients_mock.return_value = ["foouser"]
        mock.args = {"backend": 1}

        recipients_get()
        response_mock.assert_called_with(500, "error",
                                         "Custom error occurred.")


def test_recipients_get_error2():
    """
    Test recipients get if an unkown error occurs
    """
    request = "notipyserver.handlers.recipients.request"
    get_rec = "notipyserver.handlers.recipients.get_recipients"
    response = "notipyserver.handlers.recipients.create_response"

    with patch(request) as mock, patch(get_rec) as recipients_mock, \
            patch(response) as response_mock:

        recipients_mock.side_effect = ValueError()

        recipients_mock.return_value = ["foouser"]
        mock.args = {"backend": 1}

        recipients_get()
        response_mock.assert_called_with(500, "error",
                                         "An unknown error occurred.")
