from main_imports import MDScreen
from libs.applibs import utils
from libs.Firebase.CreateUser import CreateUser

utils.load_kv("signup.kv")


class Signup_Screen(MDScreen):
    def userCreate(self, func, mail, username, password):
        user = {
            "mail": mail,
            "username": username,
            "password": password
        }
        CreateUser.userCreatingWithFirebase(user)
        func.change_screen("home")
