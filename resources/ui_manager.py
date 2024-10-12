# BUTM Intro Project 2024
# Team 1

# Written by Thomas Shin

# This is the ui manager file that will be called into client.py


# ui_manager.py

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import resources.netcode as net  # Import the homemade netcode package for TCP communication

# Main application class for Kivy UI that displays sensor data
class SensorUI(App):
    def __init__(self, **kwargs):
        # Initialize Kivy App and TCP client settings
        super().__init__(**kwargs)
        self.client = net.TCPClient()  # Create new TCPClient instance
        self.client.set_server_address("192.168.1.2", 65432)  # Set server IP (Raspberry Pi's IP) and port
        self.client.connect_to_server()  # Establish connection to the TCP server

        # Initialize Labels to display data from both sensors
        self.ir_label = Label(text="IR Sensor: Connecting...")  # Label for IR sensor data
        self.ultrasonic_label = Label(text="Ultrasonic Sensor: Connecting...")  # Label for ultrasonic sensor data

    def build(self):
        # Set up layout and add both sensor labels to the UI
        layout = BoxLayout(orientation='vertical')  # Create vertical box layout
        layout.add_widget(self.ir_label)  # Add IR sensor label to the layout
        layout.add_widget(self.ultrasonic_label)  # Add ultrasonic sensor label to the layout

        # Schedule updates for both sensors every second
        Clock.schedule_interval(self.update_sensor_data, 1)  # Set update interval to 1 second
        return layout  # Return layout containing the labels

    def update_sensor_data(self, dt):
        """
        Periodically called to request data from both sensors and update the labels.
        This method runs every second, as scheduled in the build method.
        """
        try:
            # Request IR sensor data from server
            ir_data = self.client.send_request("ir")
            # Update the IR sensor label with received data
            self.ir_label.text = f"IR Sensor Data: {ir_data}"

            # Request ultrasonic sensor data from server
            ultrasonic_data = self.client.send_request("ultrasonic")
            # Update the ultrasonic sensor label with received data
            self.ultrasonic_label.text = f"Ultrasonic Sensor Data: {ultrasonic_data}"
        except Exception as e:
            # If there is an error in requesting data, update labels to show the error
            self.ir_label.text = f"IR Sensor Error: {e}"  # Display error for IR sensor
            self.ultrasonic_label.text = f"Ultrasonic Sensor Error: {e}"  # Display error for ultrasonic sensor

# Function to start Kivy UI application
def start_ui():
    SensorUI().run()  # Run SensorUI application
