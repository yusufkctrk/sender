import datetime
from libs.Firebase.sendMessageToDB import sendMessageToDB
from main_imports import MDCard, MDLabel, MDScreen, MDSeparator
from libs.applibs import utils

utils.load_kv("chat_room.kv")


class Chat_Room_Screen(MDScreen):
    partnerUsername = ""
    run = True

    def __init__(self, **kw):
        super().__init__(**kw)

    def setPartnerUsername(self, username):
        self.partnerUsername = username
        print("user" + str(username))

    def chat_textbox(self):

        fixed_Y_size = self.ids.root_chatroom.size[1] / 3
        msg_textbox = self.ids.msg_textbox.size
        if msg_textbox[1] <= fixed_Y_size:
            self.ids.send_card.size[1] = msg_textbox[1]
        else:
            self.ids.send_card.size[1] = fixed_Y_size

    def send_msg(self, msg_data):



        text_msg = MDLabel(text=msg_data, halign="right")

        sizeX = self.ids.msg_textbox.size[0]

        sizeY = self.ids.msg_textbox.size[1] + 60

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
