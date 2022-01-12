from libs.Firebase.listUsers import listUsers
from libs.uix.Constants.Params import Params
from libs.uix.User.ProfileData import ProfileData
from libs.uix.baseclass.home import Home_Screen
from main_imports import MDScreen
from libs.applibs import utils
from libs.Firebase.CreateUser import CreateUser

utils.load_kv("signup.kv")


class Signup_Screen(MDScreen):
    currentUser = {}
    users = {}
    def userCreate(self, screenChanger, mail, username, password, fullname):
        user = {
            Params.mail: mail,
            Params.fullname: fullname,
            Params.username: username,
            Params.password: password,
            Params.profileUrl: "https://firebasestorage.googleapis.com/v0/b/python-project-cb18d.appspot.com/o/profile%2Fprofile.jpg?alt=media&token=a075a91e-6035-49bc-9f8f-1962c317a281"
        }
        CreateUser.userCreatingWithFirebase(user)
        screenChanger.change_screen("home")
        listUsers(self)
        ProfileData.currentUser = user
