# BUTM Intro Project 2024
# Team 1

# Written by Thomas Shin

# This is the ui manager file that will be called into client.py


# ui_manager.py

from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from client import get_IR_sensor
from client import get_Ultrasonic_sensor
import resources.netcode as net

# The main application class for the UI to display sensor data
class SensorUI(App):
    client = None
    def __init__(self, **kwargs):
        # Initialize Kivy App and TCP client settings
        super().__init__(**kwargs)

        self.label = Label(text="Connecting to server...")  # Display initial connection status

    def build(self):
        # Sets up the Kivy UI layout and schedules periodic data requests
        # Schedule the update_sensor_data method to run every second
        Clock.schedule_interval(self.update_sensor_data, 1)  # Interval: 1 second
        return self.label  # Return the label to display on the screen

    def update_sensor_data(self, dt):
        """
        Periodically called by Kivy's Clock to request IR sensor data from the server.
        Updates the UI label with the sensor data or displays an error if it fails.
        """
        try:
            # Send a request to the server for IR sensor data
            ir_data = get_IR_sensor()
            us_data = get_Ultrasonic_sensor()
            # Update the label with the received sensor data
            self.label.text = f"IR Sensor Data: {ir_data}"
        except Exception as e:
            # Display error message if request fails
            self.label.text = f"Error: {e}"

    def set_client(self, client):
        self.client = client

# Function to start the Kivy UI application
def start_ui(client):
    ui = SensorUI()
    ui.set_client(client)
    ui.run()
    
