"""
`notipyserver` - User-Notification-Framework server

Provides test cases for the notipyserver messagehandler module.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
from mock import patch
from nose.tools import assert_equal, assert_raises

from notipyserver.backends.telegram.messagehandler import get_telegram_bot
from notipyserver.backends.telegram.messagehandler import send
from notipyserver.backends.telegram.messagehandler import send_to_group
from notipyserver.backends.telegram.errors import TelegramConfigurationError
from notipyserver.backends.telegram.errors import UserNotRegisteredError
from notipyserver.backends.telegram.errors import GroupNotRegisteredError


def test_get_telegram_bot_fail():
    """
    Test get telegram bot if it fails
    """
    with patch("notipyserver.backends.telegram.messagehandler.Config") \
            as mock, \
            patch("notipyserver.backends.telegram.messagehandler.Bot"):

        mock.side_effect = FileNotFoundError()
        assert_raises(TelegramConfigurationError, get_telegram_bot)


def test_send():
    """
    Test send
    """
    get_bot = "notipyserver.backends.telegram.messagehandler.get_telegram_bot"
    get_chat = "notipyserver.backends.telegram.messagehandler.get_user_chat_id"
    with patch(get_bot), patch(get_chat) as mock:
        send("foouser", "foobar")
        mock.assert_called_with("foouser")


def test_send_not_registered():
    """
    Test send if the user is not registered
    """
    get_bot = "notipyserver.backends.telegram.messagehandler.get_telegram_bot"
    get_chat = "notipyserver.backends.telegram.messagehandler.get_user_chat_id"
    with patch(get_bot), patch(get_chat) as mock:
        mock.side_effect = UserNotRegisteredError()

        assert_raises(UserNotRegisteredError, send, "foouser", "foobar")
        mock.assert_called_with("foouser")


def test_send_to_group():
    """
    Test send_to_group
    """
    get_bot = "notipyserver.backends.telegram.messagehandler.get_telegram_bot"
    get_cht = "notipyserver.backends.telegram.messagehandler.get_group_chat_id"
    with patch(get_bot), patch(get_cht) as mock:
        send_to_group("foogroup", "foobar")
        mock.assert_called_with("foogroup")


def test_send_to_group_not_regisd():
    """
    Test send_to_group if group is not registered
    """
    get_bot = "notipyserver.backends.telegram.messagehandler.get_telegram_bot"
    get_cht = "notipyserver.backends.telegram.messagehandler.get_group_chat_id"
    with patch(get_bot), patch(get_cht) as mock:
        mock.side_effect = GroupNotRegisteredError()

        assert_raises(GroupNotRegisteredError, send_to_group, "foogroup",
                      "foobar")
        mock.assert_called_with("foogroup")
