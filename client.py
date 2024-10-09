# BUTM Intro Project 2024
# Team 1

# Written by Jack Justus

# This is main file to run on the UI Laptop
# It will setup a TCP client using the netcode library
# It will periodically request sensor data
# It will run a UI using the _________________ library

# Client IP: 192.168.1.3/24

import resources.netcode as net
import time



# ---------------CLIENT SETUP------------------
laptopClient = net.TCPClient()
# laptopClient.set_server_address('127.0.0.1', 65432)
laptopClient.connect_to_server()




# TODO: Launch UI
from resources.ui_manager import start_ui

if __name__ == "__main__":
    start_ui()


while True:


    time.sleep(0.1)
    ir = laptopClient.send_request("ir")
