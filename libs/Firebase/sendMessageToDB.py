from libs.Firebase.firebase_config import database


def sendMessageToDB(message):
    messageData = {
        "owner": "dfkgbdf",
        "sent_to": "dfkjgdbf",
        "hasSeen": "jdsnfkj",
        "sent_time": "dfkgjb",
        "message": message
    }
    database.child("John").child("messages").child("mymessages").child("message2").push(message)
