from kivymd.uix.label import MDLabel
from libs.Firebase.listUsers import listUsers
from main_imports import MDScreen
from libs.applibs import utils
from libs.uix.User.ProfileData import ProfileData
from libs.uix.baseclass.home import Home_Screen

utils.load_kv("login.kv")


class Login_Screen(MDScreen):
    currentUser = {}
    users = {}

    def __init__(self, **kw):
        super().__init__(**kw)
        listUsers(self)
        print(self.users)
        ProfileData.userList = self.users

    def login(self, screenChanger, username, password):
        for user in self.users:
            profile_data = self.users[user]["profile_data"]
            if profile_data["username"] == username and profile_data["password"] == password:
                screenChanger.change_screen("home")
                self.currentUser = {
                    "username": profile_data["username"],
                    "password": profile_data["password"],
                    "fullname": profile_data["fullname"],
                    "mail": profile_data["mail"],
                    "profile_url": profile_data["profile_url"]
                }
                ProfileData.currentUser = self.currentUser
                Home_Screen.getUserData(self, self.currentUser)
            else:
                self.add_widget(MDLabel(
                    text=f"[color=#FF5733][size=16sp]Hatalı kullanıcı adı ya da şifre girdiniz.[/size] [/color]"
                    , halign="center"
                    , markup=True
                    , pos_hint={"center_y": .53}
                    , font_style="Caption"
                ))
