"""
This script runs the application using a development server.
"""

import os
import sys

from project.libs.bottle import run, TEMPLATE_PATH, default_app, debug

app = default_app()

TEMPLATE_PATH.insert(0, './project/views/layout')
TEMPLATE_PATH.insert(1, './project/views')

if '--debug' in sys.argv[1:] or 'SERVER_DEBUG' in os.environ:
    # Debug mode will enable more verbose output in the console window.
    # It must be set at the beginning of the script.
    debug(True)


def wsgi_app():
    """Returns the application to make available through wfastcgi. This is used
    when the site is published to Microsoft Azure."""
    return app


# Defines some useful paths
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'project/static').replace('\\', '/')
HOST = os.environ.get('SERVER_HOST', 'localhost')
try:
    PORT = int(os.environ.get('SERVER_PORT', '5555'))
except ValueError:
    PORT = 5555


# routes contains the HTTP handlers for our server and must be imported.
import project.routes.api
import project.routes.business
import project.routes.error
import project.routes.static


if __name__ == '__main__':
    run(host=HOST, port=PORT, debug=True, reloader=True)
