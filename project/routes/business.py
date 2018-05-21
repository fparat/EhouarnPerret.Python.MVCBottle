from project.controllers.mvc.home import home
from project.controllers.mvc.samples import ajax_polling, websocket
from runserver import app


@app.get('/index')
@app.get('/home')
@app.get('/')
def index():
    return home()


@app.get('/samples/ajax-polling')
def sample_ajax_polling():
    return ajax_polling()


@app.get('/samples/websocket')
def sample_websocket():
    return websocket()
