"""
`notipyserver` - User-Notification-Framework server

Provides test cases for the notipyserver config module.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
from pathlib import Path

from nose.tools import assert_equal, assert_raises

from notipyserver.config import get_token


def test_get_token():
    """
    Test get token
    """
    with (Path.home() / ".telegram-token.txt").open(mode="w+") as _file:
        _file.write("FOOTOKEN")

    assert_equal(get_token(), "FOOTOKEN")


def test_get_token_empty():
    """
    Test get token if token file is empty
    """
    with (Path.home() / ".telegram-token.txt").open(mode="w+") as _file:
        _file.write("")

    assert_raises(ValueError, get_token)
