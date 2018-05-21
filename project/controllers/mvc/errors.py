from project.libs.bottle import redirect
from project.helpers.metadata import extended_template


def not_found():
    return extended_template(inner_template='error404.html')
