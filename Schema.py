from mongoengine import Document, StringField, LongField, FloatField

class TimeSeries(Document):
    meta = {
        'strict': True,
        'collection': 'time_series',
    }
    date = StringField(required=True)
    value = LongField(required=True)
    percentage_change = FloatField(required=True)
