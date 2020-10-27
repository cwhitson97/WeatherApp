#Main page of the application
#presents users with options to create an account or sign in to an existing account
#goes alongside main.kv file

import kivy
from kivy.app import App
from kivy.uix.widget import Widget

class MainPage(Widget):
    pass

class MainApp(App):
    def build(self):
        self.title= 'Weather App'
        return MainPage()

if __name__ == '__main__':
    MainApp().run()