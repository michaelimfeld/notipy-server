"""
`notipyserver` - User-Notification-Framework server

Provides test cases for the notipyserver config module.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
import tempfile
from pathlib import Path

from nose.tools import assert_equal, assert_raises
from mock import patch

from notipyserver.config import Config
from notipyserver.errors import NoConfigurationError


def test_load_config_no_config():
    """
    Test the behaviour of load config if the config file does not exist
    """
    cfg = Config(config_path=Path("/some/non/existent/path"))
    assert_raises(NoConfigurationError, cfg.load_config)


def test_load_config():
    """
    Test loading of a configuration file
    """
    file_content = "telegram_token: 'myfootoken'\n"
    tmp_file = tempfile.TemporaryFile(suffix=".yml")

    with Path(str(tmp_file.name) + ".yml").open(mode="w+") as _file:
        _file.write(file_content)

    cfg = Config(config_path=Path(str(tmp_file.name) + ".yml"))
    assert_equal(cfg.load_config(), {"telegram_token": "myfootoken"})

    tmp_file.close()


def test_get_config_attr():
    """
    Test getting attributes from the config
    """
    with patch.object(Config, "load_config") as mock:
        mock.return_value = {"telegram_token": "foo1234"}
        cfg = Config()
        assert_equal(cfg.telegram_token, "foo1234")
