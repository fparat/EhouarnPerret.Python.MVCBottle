from project.libs.bottle import request, template

AUTHOR = "Mr Pool"
TITLE = "My Data(DeadPool) Fetcher"
HOME_URL = request.urlparts.path

DATA = {
    "Author": AUTHOR,
    "Title": TITLE,
    "HomeUrl": HOME_URL
}


def extended_template(inner_template: str, metadata=None):
    data = DATA.copy()

    if metadata and isinstance(data, dict):
        data = dict(metadata.items() + data.items())

    return template("layout.html", data=data, inner_template=inner_template)
