# --[Start platform specific code]
"""This code to detect it's Android or not
if it's not android than app window size change in android phone size"""
from kivy.utils import platform

from libs.uix.User.ProfileData import ProfileData

if platform != 'android':
    from kivy.config import Config

    Config.set("graphics", "width", 360)
    Config.set("graphics", "height", 740)
# --[End platform specific code]

# --[Start Soft_Keyboard code ]
"""code for android keyboard. when in android keyboard show textbox 
automatic go to top of keyboard so user can see when he type msg"""
from kivy.core.window import Window

Window.keyboard_anim_args = {"d": .2, "t": "linear"}
Window.softinput_mode = "below_target"
# --[End Soft_Keyboard code ]

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
    """
    Sender App start from here this class is root of app.
    in kivy (.kv) file when use app.method_name app is start from here
    """

    def __init__(self, **kwargs):
        super(SenderApp, self).__init__(**kwargs)
        self.APP_NAME = "sender"
        self.COMPANY_NAME = "message.org"

    def chat_room(self, touch, a):
        """Switch to Chatroom. but username and chatroom username
        change according to which one you touch in chat list"""
        name = touch.text
        self.screen_manager.get_screen("chat_room").ids.profile_bar.title = name
        self.screen_manager.change_screen("chat_room")

    def all_chats(self):
        """
        All Chat that show in home chat tab. all chat are added by
        this method. it will use in differe t in future.
        """
        # for dummy chats [------
        # self.change_screen("profile")

        twolineW = TwoLineAvatarListItem(text=f"Yusuf Kocatürk",
                                         secondary_text="@yusufkocaturk",
                                         on_touch_up=self.chat_room)
        twolineW.add_widget(ImageLeftWidget(
            source="https://firebasestorage.googleapis.com/v0/b/python-project-cb18d.appspot.com/o/profile%2Fprofile.jpg?alt=media&token=a075a91e-6035-49bc-9f8f-1962c317a281"))
        self.screen_manager.get_screen("home").ids.chat_tab.add_widget(twolineW)

        #  ----- ] end dummy chats

    def build(self):
        """
        This method call before on_start() method so anything
        that need before start application all other method and code
        write here.
        """
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
        """
        Anything we want to run when start application that code is here.
        """
        self.screen_manager.change_screen("login")
        self.all_chats()


if __name__ == "__main__":
    # Start application from here.
    SenderApp().run()
