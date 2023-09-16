from app.profile import bp
from app.extensions import mongo

from flask import render_template

@bp.route('/<username>')
def index(username):
    db = mongo.cx["Mindblown"]
    Users = db["User"]
    Daily = db["Daily"]
    userID = Users.find_one({"name": username})["UID"]
    dailyData = Daily.find({"UID": userID})
    #convert dailyData to list
    dailyData = list(dailyData)
    return render_template('profile/index.html', dailyData=dailyData)