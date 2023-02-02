from server.api.route import init_api_blueprint
from application import application

application.register_blueprint(init_api_blueprint())

if __name__ =="__main__":
    application.run(host='0.0.0.0',debug=True)