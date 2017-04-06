"""
`notipyserver` - User-Notification-Framework server

Provides test cases for the notipyserver response module.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
from mock import patch

from notipyserver.response import create_response


def test_create_response():
    """
    Test create response
    """
    with patch("notipyserver.response.make_response") as mock:
        create_response(200, "success", "foo", None)
        assert(mock.called)
