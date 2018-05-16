from project.libs.bottle import static_file, get


# (Agnostic) Static Routes
@get('/<filename:path>')
def send_static(filename):
    return static_file(filename, root='project/static/')

