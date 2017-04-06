"""
`notipyserver` - User-Notification-Framework server

Provides test cases for the notipyserver userregistration module.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
from mock import patch, MagicMock
from nose.tools import assert_equal, assert_raises
import telegram

from notipyserver.backends.telegram.userregistration import register


def test_register_user_no_username():
    """
    Test register user if the user has no username
    """
    bot = MagicMock()
    bot.sendMessage = MagicMock()

    update = MagicMock()
    update.message.chat.type = "private"
    update.message.chat.username = ""
    update.message.chat_id = 1234

    register(bot, update)

    bot.sendMessage.assert_called_with(
        chat_id=1234, text="Please setup a telegram username to use this bot.")


def test_register_user():
    """
    Test register user
    """
    bot = MagicMock()
    bot.sendMessage = MagicMock()

    update = MagicMock()
    update.message.chat.type = "private"
    update.message.chat.username = "foouser"
    update.message.chat.first_name = "Foo"
    update.message.chat_id = 1234

    add_user = "notipyserver.backends.telegram.userregistration.add_user"

    with patch(add_user) as mock:
        mock.return_value = True
        register(bot, update)

        bot.sendMessage.assert_called_with(
            chat_id=1234,
            text="Hi Foo!\nYour registration was *successful* 🎉.",
            parse_mode=telegram.ParseMode.MARKDOWN)


def test_register_user_already_reg():
    """
    Test register user if the user is already registered
    """
    bot = MagicMock()
    bot.sendMessage = MagicMock()

    update = MagicMock()
    update.message.chat.type = "private"
    update.message.chat.username = "foouser"
    update.message.chat.first_name = "Foo"
    update.message.chat_id = 1234

    add_user = "notipyserver.backends.telegram.userregistration.add_user"

    with patch(add_user) as mock:
        mock.return_value = False
        register(bot, update)

        bot.sendMessage.assert_called_with(
            chat_id=1234,
            text="Already registered!",
            parse_mode=telegram.ParseMode.MARKDOWN)


def test_register_group():
    """
    Test register group
    """
    bot = MagicMock()
    bot.sendMessage = MagicMock()

    update = MagicMock()
    update.message.chat.type = "group"
    update.message.chat.username = None
    update.message.chat.first_name = None
    update.message.chat_id = 1234
    update.message.chat.title = "Test Group"

    add_group = "notipyserver.backends.telegram.userregistration.add_group"

    with patch(add_group) as mock:
        mock.return_value = True
        register(bot, update)

        bot.sendMessage.assert_called_with(
            chat_id=1234,
            text="Hi Test Group!\nYour registration was *successful* 🎉.",
            parse_mode=telegram.ParseMode.MARKDOWN)
