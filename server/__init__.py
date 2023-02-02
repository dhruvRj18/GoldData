from flask_mongoengine import MongoEngine
from flask_marshmallow import Marshmallow

from server.application import application

ma = Marshmallow(application)
db = MongoEngine()
db.init_app(application)