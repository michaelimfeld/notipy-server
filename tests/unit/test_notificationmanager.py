"""
`notipyserver` - User-Notification-Framework server

Provides test cases for the notipyserver notificationmanager module.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
from mock import patch
from nose.tools import assert_equal, assert_raises

from notipyserver.notificationmanager import dispatch_notification
from notipyserver.errors import BackendNotFoundError


def test_dispatch_notification():
    """
    Test dispatch notification
    """
    tel_hand = "notipyserver.notificationmanager.telegram_handler"
    with patch(tel_hand) as mock:
        dispatch_notification(1, "foouser", "foobar")
        mock.assert_called_with("foouser", "foobar")


def test_dispatch_notification_fail():
    """
    Test dispatch notification if backend can not be found
    """
    assert_raises(BackendNotFoundError, dispatch_notification, 9999, "foouser",
                  "foobar")
