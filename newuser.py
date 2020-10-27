#NewUsers part of the application
#allows new users to create an account
#goes alongside new.kv file

import kivy
from kivy.app import App
from kivy.uix.widget import Widget

class NewPage(Widget):
    pass

class NewApp(App):
    def build(self):
        self.title= 'New User'
        return NewPage()

if __name__ == '__main__':
    NewApp().run()