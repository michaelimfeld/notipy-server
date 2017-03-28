"""
`notipyserver` - User-Notification-Framework server

Provides the flask application object.

:copyright: (c) by Michael Imfeld
:license: MIT, see LICENSE for details
"""
from flask import Flask

app = Flask(__name__)  # pylint: disable=invalid-name
