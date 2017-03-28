"""
`notipyserver` - User-Notification-Framework server

Provides test cases for the notipyserver usermanager module.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
import tempfile
from pathlib import Path

from mock import patch
from nose.tools import assert_equal, assert_true, assert_false, assert_raises

from notipyserver.backends.telegram.usermanager import load_yaml_file
from notipyserver.backends.telegram.usermanager import add_user
from notipyserver.backends.telegram.usermanager import add_group
from notipyserver.backends.telegram.usermanager import get_user_chat_id
from notipyserver.backends.telegram.usermanager import get_group_chat_id
from notipyserver.backends.telegram.usermanager import get_users
from notipyserver.backends.telegram.usermanager import get_groups

from notipyserver.backends.telegram.errors import UserNotRegisteredError
from notipyserver.backends.telegram.errors import GroupNotRegisteredError


def test_load_yaml_file_no_f():
    """
    Test load yaml file if the file does not exist
    """
    path = Path("/foobar/nonexistentyamlfile")
    assert_equal(load_yaml_file(path), {})


def test_load_yaml_file():
    """
    Test load yaml file
    """
    file_content = "foouser: 1234\nbaruser: 4321"
    tmp_file = tempfile.TemporaryFile(suffix=".yml")

    with Path(str(tmp_file.name) + ".yml").open(mode="w+") as _file:
        _file.write(file_content)

    res = load_yaml_file(Path(str(tmp_file.name) + ".yml"))
    assert_equal(res, {"foouser": 1234, "baruser": 4321})

    tmp_file.close()


def test_add_user_new_user():
    """
    Test add user if the user is not registered yet
    """
    load_yml = "notipyserver.backends.telegram.usermanager.load_yaml_file"
    with patch(load_yml) as mock:
        mock.return_value = {"foouser": 1234}

        (Path.home() / ".notipy").mkdir(exist_ok=True)
        assert_true(add_user("baruser", 4321))


def test_add_user_existing_user():
    """
    Test add user if the user is already registered
    """
    load_yml = "notipyserver.backends.telegram.usermanager.load_yaml_file"
    with patch(load_yml) as mock:
        mock.return_value = {"foouser": 1234}

        (Path.home() / ".notipy").mkdir(exist_ok=True)
        assert_false(add_user("foouser", 4321))


def test_add_group_new_group():
    """
    Test add group if the group is not registered yet
    """
    load_yml = "notipyserver.backends.telegram.usermanager.load_yaml_file"
    with patch(load_yml) as mock:
        mock.return_value = {"foogroup": 1234}

        (Path.home() / ".notipy").mkdir(exist_ok=True)
        assert_true(add_group("bargroup", 4321))


def test_add_group_existing_group():
    """
    Test add group if the group is already registered
    """
    load_yml = "notipyserver.backends.telegram.usermanager.load_yaml_file"
    with patch(load_yml) as mock:
        mock.return_value = {"foogroup": 1234}

        (Path.home() / ".notipy").mkdir(exist_ok=True)
        assert_false(add_group("foogroup", 4321))


def test_get_user_chat_id():
    """
    Test get user chat_id
    """
    load_yml = "notipyserver.backends.telegram.usermanager.load_yaml_file"
    with patch(load_yml) as mock:
        mock.return_value = {"foouser": 1234}

        assert_equal(get_user_chat_id("foouser"), 1234)


def test_get_user_chat_id_fail():
    """
    Test get user chat_id if the user is not registered
    """
    load_yml = "notipyserver.backends.telegram.usermanager.load_yaml_file"
    with patch(load_yml) as mock:
        mock.return_value = {"foouser": 1234}

        assert_raises(UserNotRegisteredError, get_user_chat_id, "baruser")


def test_get_group_chat_id():
    """
    Test get group chat_id
    """
    load_yml = "notipyserver.backends.telegram.usermanager.load_yaml_file"
    with patch(load_yml) as mock:
        mock.return_value = {"foogroup": 1234}

        assert_equal(get_group_chat_id("foogroup"), 1234)


def test_get_group_chat_id_fail():
    """
    Test get group chat_id if the group is not registered
    """
    load_yml = "notipyserver.backends.telegram.usermanager.load_yaml_file"
    with patch(load_yml) as mock:
        mock.return_value = {"foogroup": 1234}

        assert_raises(GroupNotRegisteredError, get_group_chat_id, "bargroup")


def test_get_users():
    """
    Test get users
    """
    load_yml = "notipyserver.backends.telegram.usermanager.load_yaml_file"
    with patch(load_yml) as mock:
        mock.return_value = {"foouser": 1234}

        assert_equal(get_users(), ["foouser"])


def test_get_groups():
    """
    Test get groups
    """
    load_yml = "notipyserver.backends.telegram.usermanager.load_yaml_file"
    with patch(load_yml) as mock:
        mock.return_value = {"foogroup": 1234}

        assert_equal(get_groups(), ["foogroup"])
