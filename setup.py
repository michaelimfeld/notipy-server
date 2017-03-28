"""
`notipyserver` - User-Notification-Framework server

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
from setuptools import setup, find_packages

setup(
    name="notipyserver",

    install_requires=[],
    packages=find_packages(exclude=("tests",)),
    entry_points={
        "console_scripts": [
            "notipyserver = notipyserver.__main__:main",
        ],
    },
)
