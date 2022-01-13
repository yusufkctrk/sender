from kivy.uix.widget import Widget

from libs.uix.Constants.Params import Params
from libs.uix.User.ProfileData import ProfileData
from libs.uix.baseclass.chat_room import Chat_Room_Screen
from libs.uix.baseclass.root import Root

from main_imports import ImageLeftWidget, MDScreen, TwoLineAvatarListItem
from libs.applibs import utils

utils.load_kv("home.kv")


class Home_Screen(MDScreen):
    username = ""
    password = ""
    mail = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for user in ProfileData.userList.values():
            twolineW = TwoLineAvatarListItem(text=user[Params.profileData][Params.fullname],

                                             on_release=lambda x: yonlendir(self, user),
                                             secondary_text=user[Params.profileData][
                                                 Params.username])
            twolineW.add_widget(ImageLeftWidget(source=user[Params.profileData][Params.profileUrl]))

            self.ids.search_items.add_widget(twolineW)

        def yonlendir(self, user):
            print(user)
            Chat_Room_Screen.setPartnerUsername(self, user)

    def getUserData(self, userDict):
        self.username = userDict[Params.username],
        self.password = userDict[Params.password],
        self.mail = userDict[Params.mail]
