from flask import Flask

from config import Config
from app.extensions import mongo

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    #initialize the flask extensions here
    mongo.init_app(app)
    # db = mongo.cx["Mindblown"]
    # print(db.list_collection_names())
    
    #register the blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.game import bp as game_bp
    app.register_blueprint(game_bp, url_prefix='/game')

    from app.profile import bp as profile_bp
    app.register_blueprint(profile_bp, url_prefix='/profile')

    @app.route('/test')
    def test():
        return "Hello World!"

    return app