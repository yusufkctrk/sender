import datetime

from libs.Firebase.firebase_config import database
from libs.uix.Constants.Params import Params
from libs.uix.User.ProfileData import ProfileData


def sendMessageToDB(message):
    messageData = {
        Params.owner: ProfileData.currentUser[Params.username],
        Params.sentTo: "yusufkocaturk",
        Params.sentTime: str(datetime.datetime.now()),
        Params.message: message
    }
    database.child("messages").child(ProfileData.currentUser[Params.username]).child("yusufkocaturk").push(messageData)
