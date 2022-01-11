from libs.Firebase.firebase_config import database, auth


class CreateUser:

    def userCreatingWithFirebase(user):
        # print(user["username"])
        database.child("users").child(user["username"]).child("profile_data").set(user)
