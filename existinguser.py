import kivy
from kivy.app import App
from kivy.uix.widget import Widget

class ExistingPage(Widget):
    pass

class ExistingApp(App):
    def build(self):
        self.title= 'Existing User'
        return ExistingPage()

if __name__ == '__main__':
    ExistingApp().run()