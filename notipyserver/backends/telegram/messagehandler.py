"""
`notipyserver` - User-Notification-Framework server

Provides functions to send messages
to Telegram clients.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
import logging

from telegram import Bot, TelegramError

from notipyserver.config import Config

from .usermanager import get_user_chat_id, get_group_chat_id
from .errors import TelegramConfigurationError


def get_telegram_bot():
    """
    Creates a telegram bot instance.

    Returns:
        telegram.Bot: The bot instance.

    Raises:
        TelegramConfigurationError: If the telegram bot was not properly
            configured.
    """
    logger = logging.getLogger()
    try:
        return Bot(Config().telegram_token)
    except (FileNotFoundError, ValueError, TelegramError) as exc:
        logger.error("Telegram token not present or invalid: '%s'", str(exc))
        raise TelegramConfigurationError("Telegram token not "
                                         "present or invalid.")


def send(recipient, message, **_):
    """
    Sends the given message to the given
    recipient over the telegram api.

    Args:
        recipient (str): The recipient of the message.
        message (str): The message to be sent.
    Raises:
        UserNotRegisteredError: If the recipient is not registered.
        TelegramConfigurationError: If the telegram bot was not properly
            configured.
    """
    bot = get_telegram_bot()
    chat_id = get_user_chat_id(recipient)
    bot.sendMessage(chat_id=chat_id, text=message)


def send_to_group(recipient, message, **_):
    """
    Sends the given message to the given
    group recipient over the telegram api.

    Args:
        recipient (str): The recipient of the message.
        message (str): The message to be sent.
    Raises:
        GroupNotRegisteredError: If the recipient is not registered.
        TelegramConfigurationError: If the telegram bot was not properly
            configured.
    """
    bot = get_telegram_bot()

    chat_id = get_group_chat_id(recipient)
    bot.sendMessage(chat_id=chat_id, text=message)
