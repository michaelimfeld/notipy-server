"""
`notipyserver` - User-Notification-Framework server

Provides the the notipy api server.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
import time
import signal
import logging
from threading import Thread

import click
from telegram.ext import Updater, CommandHandler

# The following imports are needed for the flask route dispatching
import notipyserver.handlers.recipients  # pylint: disable=unused-import
import notipyserver.handlers.notifications  # pylint: disable=unused-import

from .app import app
from .config import Config
from .backends.telegram.userregistration import register

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


def get_telegram_updater():
    """
    Sets up a telegram updater and registers
    a new command handler for the command '/start'
    on the updater.

    Returns:
        telegram.ext.Updater: The telegram updater object.
    """
    updater = Updater(Config().telegram_token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", register))
    return updater


class NotipyServer:
    """
    Provides functions to start and stop
    the notipy server.

    Args:
        host (str): The api server's host.
        port (int): The api server's port.
    """
    def __init__(self, host, port):
        signal.signal(signal.SIGTERM, self.signal_handler)
        signal.signal(signal.SIGINT, self.signal_handler)

        self._app = Thread(target=app.run, kwargs={"host": host, "port": port})
        self._app.daemon = True
        self._updater = get_telegram_updater()
        self._up = False

    def signal_handler(self, *_):
        """
        Stops the updater thread.
        """
        self._updater.stop()
        self._up = False

    def start(self):
        """
        Starts the Telegram updater and
        the flask rest api server.
        """
        self._up = True
        self._app.start()
        self._updater.start_polling()
        while self._up:
            time.sleep(1)


@click.command()
@click.option("--host", default="0.0.0.0", help="Webserver host.")
@click.option("--port", default=5000, help="Webserver port.")
def main(host, port):
    """
    Starts the flask application and the
    telegram bot.
    """
    NotipyServer(host, port).start()
