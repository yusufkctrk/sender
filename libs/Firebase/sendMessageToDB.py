from libs.Firebase.firebase_config import database


def sendMessageToDB(message):
    database.child("John").child("messages").child("mymessages").child("message2").push(message)
