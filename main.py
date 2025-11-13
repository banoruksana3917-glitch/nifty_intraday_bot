from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import random

from app.ui_helper import get_signal

class MainScreen(BoxLayout):
    def update_signal(self, *args):
        signal = get_signal()
        self.ids.signal_label.text = f"📈 ट्रेड सिग्नल: {signal}"

class NiftyBotApp(App):
    def build(self):
        screen = MainScreen()
        Clock.schedule_interval(screen.update_signal, 10)
        return screen

if __name__ == "__main__":
    NiftyBotApp().run()
