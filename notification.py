#Notification part of the application
#Presents users with a notification of tips & suggestions based on the weather outside
#goes alongside weather.kv file

import kivy
from kivy.app import App
from kivy.uix.widget import Widget

class WeatherPage(Widget):
    pass

class WeatherApp(App):
    def build(self):
        self.title= 'Weather Notification'
        return WeatherPage()

if __name__ == '__main__':
    WeatherApp().run()