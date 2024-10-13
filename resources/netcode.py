# BUTM Intro Project 2024
# Team 1

# Written by Jack Justus

# This is the network code for the TCP communication between the pi & laptop
# The laptop will request data from the Pi periodically.
# The client will read the response and pass it off to the UI Controller
# Static IPs must be set up on both devices for this to work.





import socket
import constants
class TCPClient:
    # This class enables a TCP Network connection with a TCP Server

    connection = None               # Socket object
    server_ip = constants.pi_IP_ADDRESS
    server_port = constants.router_to_PI_PORT

    connection_active = False


    def __init__(self):
        # Create a TCP/IP Socket
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # AF_INET = IPv4, SOCK_STREAM = TCP


    def connect_to_server(self):
        try:
            server_address = (self.server_ip, self.server_port)

            # Establish a connection with the TCP server at server_address
            self.connection.connect(server_address)
            self.connection_active = True

        except ConnectionRefusedError:
            # If there is no TCP Server at the address, this will run.
            print("Error: Connection Refused. (Is the server running?)")


    def send_request(self, request):
        try:
            # Encode the request
            request = request.encode()

            # Send the request to the server
            self.connection.send(request)

            # Wait for the response
            response = self.connection.recv(1024).decode()

            print(f'Response from server: {response}')
            return response
        
        except BrokenPipeError:
            print("Error: Broken Pipe. (Is the server running?)")
        
        
    def close_connection(self):
        self.connection.close()


    def set_server_address(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port

class TCPServer:
    # This class enables functionality as a TCP Server

    server_socket = None            # Socket object for server
    server_ip = '192.168.1.2'
    server_port = 65432

    connection_active = False
    connection = None               # Socket object for connection
    client_address = None           # Address for connection

    def __init__(self):

        # Create a TCP/IP socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # AF_INET = IPv4, SOCK_STREAM = TCP


    def start_server(self):
        # Bind the socket to an IP address and port
        self.server_address = (self.server_ip, self.server_port)                 # Address & Port of server
        print(f"attempting to start on {self.server_address}")
        self.server_socket.bind(self.server_address)                             # Patching the socket object to a port

        self.server_socket.listen(1)                                             # Accept incoming connections, refuse any more than (1) connection

        print(f'TCP Server started on {self.server_ip}:{self.server_port}')


    def run(self):
        # Meant to be called every frame. 
        # Listens for incoming connections & replies to incoming packets


        if not self.connection_active:
            print("Waiting for a connection...")
            
            # Try to accept an incoming connection
            # If no connection is avaiable, this will wait until one is found
            # Once connected, Assigns socket obj to connection & address to client_address
            self.connection, self.client_address = self.server_socket.accept()

            # Connection was successful
            self.connection_active = True
            print(f"Connection from {self.client_address}")


        # TODO: Unnecessary try?
        try:

            # Receive the incoming request
            request = self.read_data()
            print(f"Received: {request}")
            return request
        
        finally:
            pass


    def read_data(self):
    
        # Recieves data from socket (up to 1024 bytes).
        data = self.connection.recv(1024)           
                 
        if data:
            return data.decode()
            

    def send_response(self, response):

        # Encode strings before sending them
        if isinstance(response, str):
            response = response.encode()
        elif isinstance(response, float):
            response = str(response).encode()
            print(f"this is an int: {response}")
        
        # Send the strings
        print(f"Sent: {response}")
        self.connection.sendall(response)


    def set_server_address(self, server_ip, server_port):
        if not self.connection_active:
            self.server_ip = server_ip
            self.server_port = server_port
        else:
            print("Failed to set server address: Server Already Running.")
            

    def close_server(self):
        self.connection.close()
        self.connection_active = False
        self.connection = None
        self.client_address = None

    # def interpret_request(self, request):

    #     # Look up the function in the table and return it
    #     if request in self.response_table:
    #         self.response_table[request]()  # Call the function
    #         response = "good"
    #     else:
    #         response = "Invalid request"
        
    #     # Send the response back to the client
    #     self.send_response(response)


    # def set_response_table(self, response_table):
    #     self.response_table = response_table



