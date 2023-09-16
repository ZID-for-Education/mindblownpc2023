from app.profile import bp
from app.extensions import mongo

from flask import render_template

@bp.route('/')
def index():
    db = mongo.cx["Mindblown"]
    username = db["User"].find_one({"name": "test"})["name"]
    return render_template('profile/index.html', username=username)