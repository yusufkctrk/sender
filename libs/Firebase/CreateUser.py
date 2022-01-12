from libs.Firebase.firebase_config import database, auth
from libs.uix.Constants.Params import Params


class CreateUser:

    def userCreatingWithFirebase(user):
        # print(user["username"])
        database.child(Params.usersRoute).child(user[Params.username]).child(Params.profileData).set(user)
