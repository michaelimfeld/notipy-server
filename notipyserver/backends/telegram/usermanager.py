"""
`notipyserver` - User-Notification-Framework server

Provides functions to read and write to the
users yaml file.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
import logging
from os.path import expanduser
from pathlib import Path
import yaml

from .errors import UserNotRegisteredError, GroupNotRegisteredError

USERS_FILE_PATH = Path(expanduser("~"), ".notipy-data", "telegram-users.yml")
GROUPS_FILE_PATH = Path(expanduser("~"), ".notipy-data", "telegram-groups.yml")


def load_yaml_file(file_path):
    """
    Reads a the given file and parses
    it using yaml.

    Args:
        file_path (pathlib.Path): The path of the yaml file.

    Returns:
        dict: The parsed data if file exists, otherwise empty dict.
    """
    if not file_path.exists():
        return dict()

    with file_path.open(encoding="utf-8") as yaml_file:
        data = yaml.load(yaml_file.read())
        return data if data else dict()


def add_user(username, chat_id):
    """ Adds a user to the users file.

    Adds a user with given username and given
    chat_id to the users file.
    If the user already exists his chat_id will
    be overwritte with the given one.

    Args:
        username (str): The user's telegram username.
        chat_id (str): The user's chat_id.

    Returns:
        bool: True if the user was added, otherwise False
    """
    logger = logging.getLogger()
    # Create directory if it does not already exist
    USERS_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Create file if it does not already exist
    USERS_FILE_PATH.touch()

    users = load_yaml_file(USERS_FILE_PATH)

    with USERS_FILE_PATH.open(mode="w", encoding="utf-8") as users_file:
        logger.info("Registering user '%s'", username)
        is_new = username not in users
        users[username] = str(chat_id)
        users_file.write(yaml.dump(users, default_flow_style=False))
        return is_new


def add_group(group_name, chat_id):
    """ Adds a group to the groups file.

    Adds a group with given name and given
    chat_id to the groups file.

    If the group already exist, it will not
    be overwritten.

    Args:
        group_name (str): The group's name.
        chat_id (str): The group's chat_id.

    Returns:
        bool: True if the user was added, otherwise False
    """
    logger = logging.getLogger()
    # Create directory if it does not already exist
    GROUPS_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Create file if it does not already exist
    GROUPS_FILE_PATH.touch()

    groups = load_yaml_file(GROUPS_FILE_PATH)
    if group_name in groups:
        return False

    with GROUPS_FILE_PATH.open(mode="w", encoding="utf-8") as groups_file:
        logger.info("Registering group '%s'", group_name)
        groups[group_name] = chat_id
        groups_file.write(yaml.dump(groups, default_flow_style=False))

    return True


def get_user_chat_id(username):
    """Gets the user's chat_id.

        Gets the user's chat_id from the users.yml
        file.

        Args:
            username (str): The user's telegram username.

        Returns:
            int: The chat_id.

        Raises:
            UserNotRegisteredError: If the given user is not registered.
    """
    users = load_yaml_file(USERS_FILE_PATH)
    chat_id = users.get(username)
    if not chat_id:
        raise UserNotRegisteredError("User '{}' is not registered"
                                     .format(username))
    return chat_id


def get_group_chat_id(group_name):
    """Gets the group's chat_id.

        Gets the group's chat_id from the groups.yml
        file.

        Args:
            group_name (str): The group's name.

        Returns:
            int: The chat_id.

        Raises:
            GroupNotRegisteredError: If the given group is not registered.
    """
    groups = load_yaml_file(GROUPS_FILE_PATH)
    chat_id = groups.get(group_name)
    if not chat_id:
        raise GroupNotRegisteredError("Group '{}' is not registered"
                                      .format(group_name))
    return chat_id


def get_users():
    """
    Gets all users from the users.yml file.

    Returns:
        list: List of users.
    """
    users = load_yaml_file(USERS_FILE_PATH)
    return list(users.keys())


def get_groups():
    """
    Gets all groups from the groups.yml file.

    Returns:
        list: List of groups.
    """
    groups = load_yaml_file(GROUPS_FILE_PATH)
    return list(groups.keys())
