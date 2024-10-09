# BUTM Intro Project 2024
# Team 1

# Written by Thomas Shin

# This is the file to ui manager code that will be called into client.py


# ui_manager.py

from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
import resources.netcode as net

class SensorUI(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client = net.TCPClient()  # Initialize TCP client
        self.client.set_server_address("192.168.1.2", 65432)  # IP of the server (Pi)
        self.client.connect_to_server()  # Connect to server
        self.label = Label(text="Connecting to server...")

    def build(self):
        # Schedule periodic sensor data requests
        Clock.schedule_interval(self.update_sensor_data, 1)  # 1 second interval
        return self.label

    def update_sensor_data(self, dt):
        try:
            # Send a request for the IR sensor data to the server
            ir_data = self.client.send_request("ir")
            self.label.text = f"IR Sensor Data: {ir_data}"
        except Exception as e:
            self.label.text = f"Error: {e}"

def start_ui():
    SensorUI().run()
