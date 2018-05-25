from project.libs.bottle import response, HTTPResponse, redirect


def simple_redirect(location, code=303):
    try:
        redirect(location, code)
    except HTTPResponse as res:
        return res
    # Alternative
    # response.status = code
    # response.set_header('Location', location)
