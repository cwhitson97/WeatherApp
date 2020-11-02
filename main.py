# Main page of the application
# presents users with options to create an account or sign in to an existing account
# goes alongside main.kv file


import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file('main.kv')
Builder.load_file('new.kv')
Builder.load_file('existing.kv')
Builder.load_file('weather.kv')
Builder.load_file('forecast.kv')


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
