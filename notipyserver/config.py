"""
`notipyserver` - User-Notification-Framework server

Provides the configuration for notipy.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
from pathlib import Path


def get_token():
    """
    Reads the telegram token from the token.txt
    configuration file.

    Raises:
        FileNotFoundError: If the token file does not exist.
        ValueError: If the token file is empty.
    """
    path = (Path.home() / ".telegram-token.txt")
    token = path.open().read().strip()
    if not token:
        raise ValueError("Token file {} is empty.".format(path))
    return token
