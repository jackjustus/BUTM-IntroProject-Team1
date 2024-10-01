from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.uix.pagelayout import PageLayout
from kivy.uix.screenmanager import Screen, ScreenManager


sm = ScreenManager()

for i in range(4):
    screen = Screen(name='title %d' % i)
    sm.add_widget(screen)

class HomeScreen(PageLayout):
    pass


# The class name has to match the top level thing in the .kv file
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass


class UIMockupApp(App):
    def build(self):

        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm
        # return HomeScreen()


if __name__ == '__main__':
    UIMockupApp().run()
