from project.libs.bottle import static_file
from runserver import app, STATIC_ROOT


# (Agnostic-ish) Static Routes
@app.get('/:path#(css|favicons|fonts|img|js)\/.+#')
def send_static(path):
    """Handler for static files, used with the development server.
    When running under a production server such as IIS or Apache,
    the server should be configured to serve the static files."""
    return static_file(path, root=STATIC_ROOT)
