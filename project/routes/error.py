from project.libs.bottle import error


@error(404)
def error404():
    return "not found"
