from kivy.core.window import Window
from main_imports import ScreenManager
from libs.applibs import utils

utils.load_kv("root.kv")


class Root(ScreenManager):
    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)
        self.screen_list = list() 

    def _key_handler(self, instance, key, *args):
        if key is 27:
            
            self.previous_screen()
            return True

    def previous_screen(self):

        last_screen = self.screen_list.pop()
        if last_screen == "home" or last_screen == "login":
            exit()
        print(self.screen_list)
        self.current = self.screen_list[len(self.screen_list) - 1]

    def change_screen(self, name, entered=True):

        self.current = name
        if (self.transition.direction):
            if (entered):
                self.transition.direction = "left"
            else:
                self.transition.direction = "right"

        if name not in self.screen_list:
            self.screen_list.append(self.current)
        else:
            self.screen_list.remove(name)
            self.screen_list.append(self.current)
        print(self.screen_list)

        if name == "home":

            self.get_screen(name).ids.android_tabs.on_resize()

    def changeScreen(self, name):
        print(name)
        self.screen_list.append(name)
