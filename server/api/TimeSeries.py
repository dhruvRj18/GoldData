from server.data_manager.data_manager import get_data
from flask import jsonify
import logging
from http import HTTPStatus
from server.schema import time_series_return_schema
from flasgger import SwaggerView

log = logging.getLogger(__name__)

class TimeSeriesViewBase(SwaggerView):
    tags = ['Data']


class GetTimeSeries(TimeSeriesViewBase):
    responses = {
        HTTPStatus.OK.value: {
            'description': 'List of Data',
        }
    }

    def get(self):
        try:
            data = get_data()
            data_dump = time_series_return_schema.dump(data)
            return jsonify(data_dump), HTTPStatus.OK
        except Exception as e:
            log.error(e)
            return None
