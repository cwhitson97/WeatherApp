import kivy
from kivy.app import App
from kivy.uix.widget import Widget

class WeatherPage(Widget):
    pass

class WeatherApp(App):
    def build(self):
        self.title= 'Weather App'
        return WeatherPage()

if __name__ == '__main__':
    WeatherApp().run()