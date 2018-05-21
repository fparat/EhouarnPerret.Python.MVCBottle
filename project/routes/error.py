from project.controllers.mvc.errors import not_found
from project.helpers.redirection import simple_redirect
from runserver import app


@app.error(404)
def on_error404(error):
    simple_redirect('/404', 303)


@app.get('/404')
def error404():
    return not_found()
