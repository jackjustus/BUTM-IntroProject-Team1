# BUTM Intro Project 2024
# Team 1

# Written by Jack Justus

# This is main file to run on the raspberry pi
# It will setup a TCP server using the netcode library
# It will poll sensor data using the _________ library
# 

# Server IP: 192.168.1.2/24

import resources.netcode as net
import resources.sensor as sensor
import time
import random
import constants

ultrasonic_sensor = sensor.sensor_data_collector(constants.trigger_pin,constants.ultrasonic_read_pin, constants.ir_read_pi, time.time())

# ---------------SENSOR GET FUNCTIONS------------------
def get_temperature():
    return random.randint(50,80)

def get_ultrasonic():
    return ultrasonic_sensor.collect_data()[0]

def get_ir():
    return ultrasonic_sensor.collect_data()[1]

def sensor_two():
    return 1





# ---------------RESPONSE TABLE------------------
# Robust way of keeping track of responses
response_table = {
    'ir': get_ir,
    'ultrasonic': get_ultrasonic,
}






# ---------------SERVER SETUP------------------
# Start the server
piServer = net.TCPServer()
piServer.set_server_address(constants.pi_IP_ADDRESS, constants.router_to_PI_PORT)
piServer.start_server()

def run_server():
    # Check for requests
    request = piServer.run()

    # Look up the function in the table and return it
    if request in response_table:
        response = response_table[request]()  # Call the function
    else:
        response = "Invalid request"
    
    # Send the response back to the client
    piServer.send_response(response)






# ---------------EVENT LOOP------------------
while True:

    run_server()


    

