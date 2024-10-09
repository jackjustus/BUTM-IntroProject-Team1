# BUTM Intro Project 2024
# Team 1

# Written by Thomas Shin

# This is the file to ui manager code that will be called into client.py


import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
import resources.netcode as net

class SensorUI(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client = net.TCPClient()
        self.client.connect_to_server()  # Connect to the TCP server
        self.label = Label(text="Fetching sensor data...")

    def build(self):
        Clock.schedule_interval(self.update_sensor_data, 1)
        return self.label

    def update_sensor_data(self, dt):
        try:
            ir_data = self.client.send_request("ir")  # Send a request to server
            self.label.text = f"IR Sensor Data: {ir_data}"
        except Exception as e:
            self.label.text = f"Connection Error: {e}"

def start_ui():
    SensorUI().run()
