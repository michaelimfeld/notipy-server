"""
`notipyserver` - User-Notification-Framework server

Provides test cases for the notipyserver recipientsmanager module.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
from mock import patch
from nose.tools import assert_equal, assert_raises

from notipyserver.recipientsmanager import get_recipients
from notipyserver.errors import BackendNotFoundError


def test_get_recipients():
    """
    Test get recipients
    """
    tel_hand = "notipyserver.notificationmanager.telegram_handler"
    with patch(tel_hand) as mock:
        mock.return_value = ["foouser"]
        res = get_recipients(1)
        assert_equal(res, ["foouser"])


def test_get_recipients_fail():
    """
    Test get recipients if backend can not be found
    """
    assert_raises(BackendNotFoundError, get_recipients, 9999)
