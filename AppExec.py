import kivy
from kivy.app import App
from kivy.uix.label import Label


class WeatherApp(App):
    def build(self):
        return Label(text="Weather App")


if __name__ == '__main__':
    WeatherApp().run()
