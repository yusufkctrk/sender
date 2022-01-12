import datetime

from libs.Firebase.firebase_config import database
from libs.Firebase.sendMessageToDB import sendMessageToDB
from libs.uix.Constants.Params import Params
from libs.uix.User.ProfileData import ProfileData
from main_imports import MDCard, MDLabel, MDScreen, MDSeparator
from libs.applibs import utils
from threading import Timer

utils.load_kv("chat_room.kv")


class Chat_Room_Screen(MDScreen):
    partnerUsername = ""
    run = True

    def __init__(self, **kw):
        super().__init__(**kw)

        def retrieveData():
            messages = database.child(Params.messages).get()
            for item in messages.each():
                if ProfileData.currentUser[Params.username]:
                    if item.key() == ProfileData.currentUser[Params.username]:
                        pass
            if self.run:
                Timer(1, retrieveData).start()

        retrieveData()

    def setPartnerUsername(self, username):
        self.partnerUsername = username
        print(username)
        g = getData()

    def chat_textbox(self):
        """
            MDCard size change when MSGbox use multilines.
            MDCard y axis size incress when MSGbox y axis size incress
        """
        fixed_Y_size = self.ids.root_chatroom.size[1] / 3
        msg_textbox = self.ids.msg_textbox.size
        if msg_textbox[1] <= fixed_Y_size:
            self.ids.send_card.size[1] = msg_textbox[1]
        else:
            self.ids.send_card.size[1] = fixed_Y_size

    def send_msg(self, msg_data):

        """
            When send button use to send msg this function call
            and clear MSGbox 
        """

        text_msg = MDLabel(text=msg_data, halign="right")

        sizeX = self.ids.msg_textbox.size[0]

        sizeY = self.ids.msg_textbox.size[1] + 60
        # ->> sizeY is equal to msg_textbox sizeY because text_msg sizeY not work 
        # that's why i use msg_textbox is called 'Jugaad'

        msg_card = MDCard(
            orientation="vertical",
            size_hint=[None, None],
            size=[sizeX, sizeY],
            spacing=8,
            padding=[20, 2, 20, 20],
            elevation=9,
            ripple_behavior=True,
            radius=[25, 25, 25, 0],
            md_bg_color=[0, 1, 1, .5]

        )
        msg_card.add_widget(MDLabel(
            text=f"Sender {' ' * 8} {datetime.datetime.now().hour}:{datetime.datetime.now().minute}",
            theme_text_color="Primary",
            size_hint_y=None,
            height=50

        ))

        msg_card.add_widget(MDSeparator(
            height="1dp"

        ))

        msg_card.add_widget(text_msg)
        self.ids.all_msgs.add_widget(msg_card)

        sendMessageToDB(msg_data)
        self.ids.msg_scroll_view.scroll_to(msg_card)
        self.ids.msg_textbox.text = ""
