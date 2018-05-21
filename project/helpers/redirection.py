from project.libs.bottle import response


def simple_redirect(location, code):
    response.status = code
    response.set_header('Location', location)
