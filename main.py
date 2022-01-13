
from kivy.utils import platform

from libs.uix.User.ProfileData import ProfileData

if platform != 'android':
    from kivy.config import Config

    Config.set("graphics", "width", 360)
    Config.set("graphics", "height", 740)

from kivy.core.window import Window

Window.keyboard_anim_args = {"d": .2, "t": "linear"}
Window.softinput_mode = "below_target"
from libs.uix.baseclass.chat_room import Chat_Room_Screen
from libs.uix.baseclass.forgot import Forgot_Screen
from libs.uix.baseclass.home import Home_Screen
from libs.uix.baseclass.login import Login_Screen
from libs.uix.baseclass.root import Root
from libs.uix.baseclass.signup import Signup_Screen
from libs.uix.baseclass.verification import Verification_Screen
from libs.uix.baseclass.create_chat_room import Create_Chat_Room
from main_imports import ImageLeftWidget, MDApp, TwoLineAvatarListItem


class SenderApp(MDApp):


    def __init__(self, **kwargs):
        super(SenderApp, self).__init__(**kwargs)
        self.APP_NAME = "sender"
        self.COMPANY_NAME = "message.org"

    def chat_room(self, touch, a):

        name = touch.text
        self.screen_manager.get_screen("chat_room").ids.profile_bar.title = name
        self.screen_manager.change_screen("chat_room")

    def all_chats(self):


        twolineW = TwoLineAvatarListItem(text=f"Yusuf Kocatürk",
                                         secondary_text="@yusufkocaturk",
                                         on_touch_up=self.chat_room)
        twolineW.add_widget(ImageLeftWidget(
            source="https://firebasestorage.googleapis.com/v0/b/python-project-cb18d.appspot.com/o/profile%2Fprofile.jpg?alt=media&token=a075a91e-6035-49bc-9f8f-1962c317a281"))
        self.screen_manager.get_screen("home").ids.chat_tab.add_widget(twolineW)

        

    def build(self):

        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.accent_hue = "500"
        self.theme_cls.theme_style = "Light"

        self.screen_manager = Root()
        self.screen_manager.add_widget(Login_Screen())
        self.screen_manager.add_widget(Signup_Screen())
        self.screen_manager.add_widget(Forgot_Screen())
        self.screen_manager.add_widget(Verification_Screen())
        self.screen_manager.add_widget(Home_Screen())
        self.screen_manager.add_widget(Chat_Room_Screen())
        self.screen_manager.add_widget(Create_Chat_Room())
        return self.screen_manager

    def on_start(self):

        self.screen_manager.change_screen("login")
        self.all_chats()


if __name__ == "__main__":
    
    SenderApp().run()
