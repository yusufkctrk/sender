from kivymd.uix.label import MDLabel
from libs.Firebase.listUsers import listUsers
from main_imports import MDScreen
from libs.applibs import utils


utils.load_kv("login.kv")


class Login_Screen(MDScreen):
    users = {}

    def __init__(self, **kw):
        super().__init__(**kw)
        listUsers(self)
        print(self.users)
    def login(self, func, username, password):
        for user in self.users:
            profile_data = self.users[user]["profile_data"]
            if profile_data["username"] == username and profile_data["password"] == password:
                func.change_screen("home")
            else:
                self.add_widget(MDLabel(
                    text=f"[color=#FF5733][size=16sp]Hatalı kullanıcı adı ya da şifre girdiniz.[/size] [/color]"
                    , halign="center"
                    , markup=True
                    , pos_hint={"center_y": .53}
                    , font_style="Caption"
                ))

