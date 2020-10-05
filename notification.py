import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.uix.widget import Widget

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        Label.color = 109/255.0,211/255.0,236/255.0,1
        self.cols = 1;
        self.inside = GridLayout()
        self.inside.cols = 2
        self.inside.add_widget(Label(text="Weather Tip of the day: ", font_size=40))

        self.notif = TextInput(multiline=False)
        self.inside.add_widget(self.notif)
        self.add_widget(self.inside)

        self.submit=Button(text="Got it!", font_size=40)
        self.submit.bind(on_press= self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        print("Notification Received")
        App.stop(self)

class MyApp(App):
    def build(self):
        self.title= 'Todays Weather Notification'

        return MyGrid()

if __name__ == '__main__':
    MyApp().run()