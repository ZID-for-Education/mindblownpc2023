from flask import Flask

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    #initialize the flask extensions here

    #register the blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    @app.route('/test')
    def index():
        return "Hello World!"

    return app