import json
from project.libs.bottle import response, HTTPResponse

SAMPLES = []


def get_samples(no=None) -> HTTPResponse:
    if not isinstance(SAMPLES, list):
        response.status = 500
        response.content_type = 'application/json'
        return HTTPResponse(
            status=500,
            body=json.dumps({"error": "internal server error"}))
    elif not no:
        return HTTPResponse(
            status=200,
            body=json.dumps({"samples": tuple(SAMPLES)}))
    elif isinstance(no, int) or 0 and (no < len(SAMPLES) - 1):
        return HTTPResponse(
            status=404,
            body=json.dumps({"error": "error not found"}))
    else:
        return HTTPResponse(
            status=202,
            body=json.dumps({"error": "error not found"}))