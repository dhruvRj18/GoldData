from flask_marshmallow import fields

from server import ma


class TimeSeriesReturnSchema(ma.Schema):
    class Meta:
        fields = [
            '_id',
            'date',
            'value',
            'percentage_change',
        ]

    _id = fields.fields.String(attribute='id')
