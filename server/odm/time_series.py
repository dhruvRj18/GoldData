from server import db


class time_series(db.Document):
    meta = {
        'strict': True,
        'collection': 'time_series',
    }
    date = db.StringField(required=True)
    value = db.LongField(required=True)
    percentage_change = db.FloatField(required=True)
