# BUTM Intro Project 2024
# Team 1

# Written by Thomas Shin

# This is the ui manager file that will be called into client.py


# ui_manager.py

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import resources.netcode as net
# from kivy_garden import matplotlib
# import matplotlib.pyplot as plt

# Main application class for Kivy UI that displays sensor data
class SensorUI(App):

    laptopClient = net.TCPClient()

    def __init__(self, **kwargs):
        # Initialize Kivy App and TCP client settings
        super().__init__(**kwargs)

        # Initialize Labels to display data from both sensors
        self.ir_label = Label(text="IR Sensor: Connecting...")  # Label for IR sensor data
        self.us_label = Label(text="Ultrasonic Sensor: Connecting...")  # Label for ultrasonic sensor data

        # Initalize graph
        # self.plt.plot([1,6,3,6,2])
        # self.plt.ylabel('some numbers')

    def build(self):
        # Set up layout and add both sensor labels to the UI
        layout = BoxLayout(orientation='vertical')  # Create vertical box layout
        layout.add_widget(self.ir_label)  # Add IR sensor label to the layout
        layout.add_widget(self.us_label)  # Add ultrasonic sensor label to the layout
        # layout.add_widget(matplotlib.FigureCanvasKivyAgg(plt.gcf()))

        # Schedule updates for both sensors every second
        Clock.schedule_interval(self.update_sensor_data, 0.2)  # Set update interval to 1 second
        return layout  # Return layout containing the labels

    def update_sensor_data(self, dt):
        """
        Periodically called to request data from both sensors and update the labels.
        This method runs every second, as scheduled in the build method.
        """
        try:
            # Send a request to the server for IR sensor data
            ir_data = self.get_IR_sensor()
            us_data = self.get_Ultrasonic_sensor()
            # Update the label with the received sensor data
            self.ir_label.text = f"IR Sensor Data: {ir_data}"
            self.us_label.text = f"US Sensor Data: {us_data}"
        except Exception as e:
            # If there is an error in requesting data, update labels to show the error
            self.ir_label.text = f"IR Sensor Error: {e}"  # Display error for IR sensor
            self.us_label.text = f"Ultrasonic Sensor Error: {e}"  # Display error for ultrasonic sensor

    def set_client(self, client):
        self.laptopClient = client
        
    def get_IR_sensor(self):
        return self.laptopClient.send_request("ir")
    def get_Ultrasonic_sensor(self):
        return self.laptopClient.send_request("ultrasonic")
    


# Function to start Kivy UI application
def start_ui():
    SensorUI().run()  # Run SensorUI application
