from libs.Firebase.firebase_config import database


def listUsers(self):
    users = database.child("users").get()
    for user in users.each():
        self.users[str(user.key())] = user.val()
