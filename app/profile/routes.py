from app.profile import bp
from app.extensions import mongo

from flask import render_template
import datetime

@bp.route('/<username>')
def index(username):
    db = mongo.cx["Mindblown"]
    Users = db["User"]
    Daily = db["Daily"]
    userID = Users.find_one({"name": username})["UID"]
    userADHD = Users.find_one({"name": username})["ADHD%"]
    if userADHD >= 50:
        userADHD = True
    currentDay = datetime.datetime.now()
    dailySet = Daily.find({"UID": userID})
    #sort the dailySet by date
    dailySet.sort("Date", 1)
    dailyData = []
    dataNum = 0
    for doc in dailySet:
            if dataNum >= 10:
                break
            #create a dictionary for each doc
            #and only add the Set No as set
            setDict = {}
            setDict["set"] = doc["Set No"]
            if userADHD:
                setDict["score"] = doc["ADHD Score"]
            else:
                setDict["score"] = doc["ASD Score"]
            dailyData.append(setDict)
            dataNum += 1
    
    return render_template('profile/index.html', dailyData=dailyData)