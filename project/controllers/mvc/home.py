from project.libs.bottle import template, request
from project.helpers.metadata import extended_template


def home():
    return extended_template('home.html')
