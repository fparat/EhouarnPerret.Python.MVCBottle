from project.libs.bottle import request, template
from project.helpers.metadata import extended_template


def ajax_polling():
    return extended_template('./samples/ajax-polling.html')


def websocket():
    return extended_template('./samples/websocket.html')
