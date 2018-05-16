from project.libs.bottle import get, template
from project.controllers.api.samples import get_samples


@get('/samples')
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


@route('/samples/<no>')
def samples(no):
    return get_samples(no)


@get('/')
def index():
    page_data = \
        {
            "author": "Mr Pool",
            "title": "My Data(DeadPool) Fetcher"
        }
    return template('home.tpl', data=page_data)
