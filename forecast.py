#Forecast part of the application
#goes alongside forecast.kv file

import kivy
from kivy.app import App
from kivy.uix.widget import Widget

class ForecastPage(Widget):
    pass

class ForecastApp(App):
    def build(self):
        self.title = 'Forecast'
        return ForecastPage()

if __name__ == '__main__':
    ForecastApp().run()