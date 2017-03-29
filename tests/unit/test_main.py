"""
`notipyserver` - User-Notification-Framework server

Provides test cases for the notipyserver main module.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
import sys
from threading import Thread
from mock import patch
from nose.tools import assert_equal

import notipyserver.__main__


def test_get_telegram_updater():
    """
    Test get telegram updater
    """
    with patch("notipyserver.__main__.Updater"), \
            patch("notipyserver.__main__.Config"):
        notipyserver.__main__.get_telegram_updater()


def test_main():
    """
    Test main
    """
    with patch("notipyserver.__main__.NotipyServer") as mock, \
            patch.object(sys, "argv", []), \
            patch.object(sys, "exit"):
        notipyserver.__main__.main()
        mock.return_value.start.assert_called_with()


def test_notipy_server():
    """
    Test instantiation of NotipyServer
    """
    with patch("notipyserver.__main__.get_telegram_updater") as mock:
        notipyserver.__main__.NotipyServer("foo", 9999)
        mock.assert_called_with()


def test_notipy_server_sig_handler():
    """
    Test signal handler of NotipyServer
    """
    with patch("notipyserver.__main__.get_telegram_updater"):
        notifier = notipyserver.__main__.NotipyServer("foo", 9999)

    with patch.object(notifier, "_updater") as mock:
        notifier.signal_handler()
        mock.stop.assert_called_with()


def test_notipy_server_start():
    """
    Test NotipyServer start
    """
    with patch("notipyserver.__main__.get_telegram_updater"):
        notifier = notipyserver.__main__.NotipyServer("foo", 9999)

    with patch.object(notifier, "_updater") as updater, \
            patch.object(notifier, "_app") as app:

        thr = Thread(target=notifier.start)
        thr.start()
        notifier.signal_handler()
        updater.start_polling.assert_called_with()
        app.start.assert_called_with()
