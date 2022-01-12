from libs.Firebase.firebase_config import database
from libs.uix.Constants.Params import Params


def listUsers(self):
    users = database.child(Params.usersRoute).get()
    for user in users.each():
        self.users[str(user.key())] = user.val()
