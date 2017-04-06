"""
`notipyserver` - User-Notification-Framework server

Provides a telegram handler function
for user registration.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
import telegram

from .usermanager import add_user, add_group


def register(bot, update):
    """
    Saves the telegram username and the chat_id from the given
    update object to a file.

    Args:
        bot (telegram.Bot): The bot instance.
        update (telegram.Update): The message update.
    """
    if update.message.chat.type == "group":
        recipient_name = update.message.chat.title
        register_function = add_group
        name = update.message.chat.title
    else:
        if not update.message.chat.username:
            message = "Please setup a telegram username to use this bot."
            bot.sendMessage(chat_id=update.message.chat_id, text=message)
            return
        recipient_name = update.message.chat.username
        register_function = add_user
        name = update.message.chat.first_name

    is_new = register_function(recipient_name, update.message.chat_id)

    if is_new:
        message = """
Hi {}!
Your registration was *successful* 🎉.
        """.format(name).strip()
    else:
        message = "Already registered!"

    bot.sendMessage(
        chat_id=update.message.chat_id,
        text=message,
        parse_mode=telegram.ParseMode.MARKDOWN)
