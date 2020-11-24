# Main page of the application
# presents users with options to create an account or sign in to an existing account
# goes alongside main.kv file

from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# ../ means going up a directory
Builder.load_file('../kv/main.kv')  # up a directory. /kv has this folder-> /kv
Builder.load_file('../kv/new.kv')
Builder.load_file('../kv/existing.kv')
Builder.load_file('../kv/weather.kv')
Builder.load_file('../kv/forecast.kv')

class NewPage(Screen):
    pass


class MainPage(Screen):
    pass


class ExistingPage(Screen):
    pass


class WeatherPage(Screen):
    pass


class ForecastPage(Screen):
    pass


screen = ScreenManager()
screen.add_widget(MainPage(name='menu'))
screen.add_widget(NewPage(name='new'))
screen.add_widget(ExistingPage(name='existing'))
screen.add_widget(WeatherPage(name='weather'))
screen.add_widget(ForecastPage(name='forecast'))


class MainApp(App):
    def build(self):
        return screen


if __name__ == '__main__':
    MainApp().run()
