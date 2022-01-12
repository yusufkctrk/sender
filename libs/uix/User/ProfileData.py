from kivy.properties import ObjectProperty

from libs.uix.Constants.Params import Params


class ProfileData:
    currentUser = {Params.username: ""}
    userList = ObjectProperty()
