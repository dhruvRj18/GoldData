import logging
from http import HTTPStatus
from flask import Blueprint,abort
from server.api.TimeSeries import GetTimeSeries

log = logging.getLogger('route')

api_blueprint = Blueprint('api', __name__, url_prefix='/api')


def init_api_blueprint():
    return api_blueprint

@api_blueprint.route('/',defaults={'path':''})
@api_blueprint.route('/<path:path>')
def index(path):
    abort(HTTPStatus.NOT_FOUND)

api_blueprint.add_url_rule(
    rule='/data',
    methods=['GET'],
    view_func= GetTimeSeries.as_view('Get Time series data')
)
