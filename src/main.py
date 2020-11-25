# Main page of the application
# presents users with options to create an account or sign in to an existing account
# goes alongside main.kv file


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from src.weather_api import *

Builder.load_file('kv/main.kv')
Builder.load_file('kv/new.kv')
Builder.load_file('kv/existing.kv')
Builder.load_file('kv/weather.kv')
Builder.load_file('kv/forecast.kv')


class NewPage(Screen):
    pass


class MainPage(Screen):
    pass


class ExistingPage(Screen):
    pass


class WeatherPage(Screen):
    pass


class ForecastPage(Screen):
    def weathertoday(self):
        self.weather = get_today_weather(self.ids.zip.text, self.ids.country.text)
        self.ids.city.text = self.weather[0] + "'s Forecast"
        return self.weather

    def weekweather(self):
        week = get_forecast_weather(self.weather[5], self.weather[4])
        self.ids.sunday.text = week[0][1] + '\n' + str(round(week[0][0], 1))
        self.ids.monday.text = week[1][1] + '\n' + str(round(week[1][0], 1))
        self.ids.tuesday.text = week[2][1] + '\n' + str(round(week[2][0], 1))
        self.ids.wednesday.text = week[3][1] + '\n' + str(round(week[3][0], 1))
        self.ids.thursday.text = week[4][1] + '\n' + str(round(week[4][0], 1))
        self.ids.friday.text = week[5][1] + '\n' + str(round(week[5][0], 1))
        self.ids.saturday.text = week[6][1] + '\n' + str(round(week[6][0], 1))


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
