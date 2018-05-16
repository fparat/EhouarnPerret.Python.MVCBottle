import os
import random
import sys
import json
import project.routes.static
import project.routes.business

from project.libs.bottle import Bottle, run, response, template, debug, static_file, route, get, TEMPLATE_PATH

app = Bottle()

dir_name = os.path.dirname(sys.argv[0])

TEMPLATE_PATH.insert(0, './project/views/layout')
TEMPLATE_PATH.insert(1, './project/views')


if __name__ == '__main__':
    run(host="localhost", port=4242, debug=True, reloader=True)
