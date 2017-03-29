"""
`notipyserver` - User-Notification-Framework server

Provides the configuration for notipy.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
from pathlib import Path
from os.path import expanduser

import yaml

from .errors import NoConfigurationError


class Config:
    """
    Provides functions to access the
    notipy configuration.

    Returns:
        dict: The parsed yaml content.
    """
    def __init__(self, config_path=Path(expanduser("~"), ".notipy.yml")):
        self.__config_path = config_path
        self.__config = dict()

    def load_config(self):
        """
        Loads the configuration file.

        Raises:
            NoConfigurationError: If the config file does not exist.
        """
        if not self.__config_path.exists():
            raise NoConfigurationError("Config file {} does not exist",
                                       str(self.__config_path))
        with self.__config_path.open() as config_file:
            return yaml.load(config_file.read())

    def __getattr__(self, name):
        self.__config = self.load_config()
        return self.__config.get(name)
