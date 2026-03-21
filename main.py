from kivy.app import App
from kivy.uix.button import Button
from kivy.clock import Clock
import webbrowser

class CyberApp(App):
    def build(self):
        return Button(text='Click to Start Test', on_press=self.start)

    def effect(self, dt):
        # يفتح المتصفح بشكل متكرر لعمل تعليق بسيط
        webbrowser.open("https://google.com/search?q=System+Test+Active")

    def start(self, instance):
        Clock.schedule_interval(self.effect, 0.5)

if __name__ == '__main__':
    CyberApp().run()
