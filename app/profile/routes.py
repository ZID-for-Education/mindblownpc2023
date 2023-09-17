from app.profile import bp
from app.extensions import mongo

from flask import render_template
import datetime

@bp.route('/0')
def index0():
    db = mongo.cx["Mindblown"]
    Users = db["User"]
    Daily = db["Daily"]
    userID = Users.find_one({"name": 'test'})["UID"]
    userADHD = Users.find_one({"name": 'test'})["ADHD%"]
    if userADHD >= 50:
        userADHD = True
    currentDay = datetime.datetime.now()
    dailySet = Daily.find({"UID": userID})
    #sort the dailySet by set no
    dailySet.sort("Set No", -1)
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
    
    #reverse the list so that the most recent set is first
    dailyData.reverse()
    
    return render_template('profile/index.html', dailyData=dailyData)


@bp.route('/1')
def index1():
    db = mongo.cx["Mindblown"]
    Users = db["User"]
    Daily = db["Daily"]
    userID = Users.find_one({"name": 'tset'})["UID"]
    userADHD = Users.find_one({"name": 'tset'})["ADHD%"]
    if userADHD >= 50:
        userADHD = True
    currentDay = datetime.datetime.now()
    dailySet = Daily.find({"UID": userID})
    #sort the dailySet by set no
    dailySet.sort("Set No", -1)
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
    
    #reverse the list so that the most recent set is first
    dailyData.reverse()
    
    return render_template('profile/index.html', dailyData=dailyData)