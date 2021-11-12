from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from mandel_lib import *
from reg_21405824 import RegisterScreen
from login_21405824 import LoginScreen
from personal_21405824 import PersonalScreen

from kivy.core.window import Window
from kivy.utils import platform
if platform in ('win', 'macosx'):
    Window.size = (414, 736)
    Window.top = 50

class HomeScreen(Screen):
    def to_login(self):
        MDApp.get_running_app().switchTo('LoginScreen')

    def to_register(self):
        MDApp.get_running_app().switchTo('RegisterScreen')

class MyApp(MDApp):
    def build(self):
        Builder.load_file('home_21405824.kv')
        Builder.load_file('reg_21405824.kv')
        Builder.load_file('login_21405824.kv')
        Builder.load_file('personal_21405824.kv')
        manager = self.manager = ScreenManager()
        manager.add_widget(HomeScreen())
        manager.add_widget(LoginScreen())
        manager.add_widget(RegisterScreen())
        manager.add_widget(PersonalScreen())
        return manager

    def switchTo(self, screen_name):
        self.manager.current = screen_name

if __name__ == '__main__' :
    MyApp().run()
