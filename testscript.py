# import time
# from visca_over_ip import Camera

# cam = Camera('192.168.0.87')  # Your camera's IP address or hostname here

# while True:
#     cam.pantilt(pan_speed=-4, tilt_speed=0)
#     time.sleep(1)  # wait one second
#     # cam.pantilt(pan_speed=1, tilt_speed=0)
#     break

import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()