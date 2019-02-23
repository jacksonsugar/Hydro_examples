from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import subprocess
import sys

def quit_slow():
    subprocess.Popen([sys.executable, "killall.py"])

class TestApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        # use a (r, g, b, a) tuple
        blue = (0, 0, 1.5, 2.5)
        red = (2.5, 0, 0, 1.5)
        btn =  Button(text='Click here!', background_color=blue, font_size=120)        
        btn.bind(on_press=self.callback)
        self.label = Label(text="------------", font_size='50sp')
        layout.add_widget(btn)
        layout.add_widget(self.label)
        return layout
    
    def callback(self, event):
        print("button touched")  # test
        self.label.text = "Button Pressed!"
	quit_slow()

TestApp().run()
