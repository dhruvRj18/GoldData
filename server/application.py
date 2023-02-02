import logging
from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from flasgger import Swagger

log_level = getattr(logging, "INFO")
logging_format = '%(asctime)s000 %(levelname)s [%(name)s] %(message)s'
logging_config = {
    'format': logging_format,
    'level': log_level,
}

logging.basicConfig(**logging_config)

log = logging.getLogger('server')
log.info('***** Starting Server *****')

application = Flask(__name__)

application.config.update({
    'MONGO_URI': "mongodb://127.0.0.1:27017/gold-data"
})

mongo = PyMongo(application)

cors = CORS(application, resources={r'/api/*': {'origins': '*'}})

log.debug('Load Api')
log.info('***** Server Started *****')

application.config['SWAGGER'] = {
    'title': 'Server APIs',
    'version' : '0.0.1',
    'swagger' : '2.0',
    'swagger_ui' : True,
}

swagger = Swagger(application)


application.config['MONGODB_SETTINGS'] = {
    'host' : "mongodb://127.0.0.1:27017/gold-data"
}
