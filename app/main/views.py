from flask import Blueprint

main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.get('/')
def page_index():
    return 'This is a main page'
