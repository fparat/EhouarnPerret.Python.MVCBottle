import json
import random

from project.controllers.api.samples import get_samples
from project.libs.bottle import response
from runserver import app


@app.get('/api/samples')
def samples():
    sample_count = random.randint(10, 30)
    column_count = 4
    cells = []

    # Let's add column Headers
    sample = ["Column {}".format(j) for j in range(column_count)]
    cells.append(sample)

    # Cells
    for i in range(sample_count):
        sample = [random.randint(-5, 5) for _ in range(column_count)]
        cells.append(sample)

    # The framework string / json is considered as 200 status code
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(cells)


@route('/upload', method='POST')
def do_upload():
    category = request.forms.get('category')
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png', '.jpg', '.jpeg'):
        return "File extension not allowed."

    save_path = "/tmp/{category}".format(category=category)
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
    upload.save(file_path)
    return "File successfully saved to '{0}'.".format(save_path)
