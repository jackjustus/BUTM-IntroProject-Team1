# BUTM Intro Project 2024
# Team 1

# Written by Jack Justus

# This is main file to run on the UI Laptop
# It will setup a TCP client using the netcode library
# It will periodically request sensor data
# It will run a UI using the tkinter library

# Client IP: 192.168.1.3/24

import resources.netcode as net
from resources.ui_manager import SensorUI, start_ui
import time
import constants


# ---------------CLIENT SETUP------------------
laptopClient = net.TCPClient()
laptopClient.set_server_address(constants.pi_IP_ADDRESS, constants.router_to_PI_PORT)
laptopClient.connect_to_server()




# ---------------UI SETUP------------------
ui = SensorUI()
ui.set_client(laptopClient)



# Nothing after this line will run until the application is closed.
ui.run()        



print("App Closed")



# ui = App()
# ui.start()


# while True:
#     ui.add_ir_data(5,time.time())
#     print("Adding data")
#     time.sleep(1)
#     print("fin")
#     ui.start()
# ui.create_ir_graph(laptopClient)