import tkinter as tk
from tkinter import LabelFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import time as runtime


class App:

    # Time data
    time = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    # Temperature data (for IR Sensor Graph)
    ir_data = [10, 90, 30, 40, 20, 60, 50, 80, 90]

    # Ultrasonic binary data (0s and 1s)
    ultrasonic_data = [1, 0, 1, 1, 0, 1, 0, 0, 1]

    def __init__(self):

        # Create the main window
        self.root = tk.Tk()
        self.root.title("BUTM Intro Project Team One")

        # Set the window size (use "geometry" if you want fixed starting size)
        self.root.geometry("800x600")
        self.root.configure(bg="black")  # Set background to black

        # Set grid weight for responsiveness
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        # Create the title label
        title_label = tk.Label(self.root, text="BUTM INTRO PROJECT TEAM ONE", font=("Courier", 24), bg="black", fg="#55ACEE")
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Create the left IR Sensor graph section
        self.ir_frame = LabelFrame(self.root, text="IR Sensor Graph", font=("Courier", 16), fg="white", bg="black", bd=5, labelanchor="n")
        self.ir_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")  # Grid makes the layout responsive

        # Create the right Ultrasonic Sensor graph section
        self.ultrasonic_frame = LabelFrame(self.root, text="Ultrasonic Graph", font=("Courier", 16), fg="white", bg="black", bd=5, labelanchor="n")
        self.ultrasonic_frame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        # Create and display the graphs in the respective sections
        self.create_ir_graph(self.ir_frame)
        self.create_ultrasonic_graph(self.ultrasonic_frame)

        

    def start(self):

        # Schedule the data updates
        self.root.after(100, self.add_ir_data)
        print("event shceudled")

        # Run the Tkinter event loop
        self.root.mainloop()

    # Function to create the IR Sensor Graph
    def create_ir_graph(self, frame):


        x = np.linspace(0, 6*np.pi, 100)
        y = np.sin(x)

        # You probably won't need this if you're embedding things in a tkinter plot...
        # plt.ion()

        fig = plt.figure()
        ax = fig.add_subplot(111)
        line1, = ax.plot(x, y, 'r-') # Returns a tuple of line objects, thus the comma

        for phase in np.linspace(0, 10*np.pi, 500):
            line1.set_ydata(np.sin(x + phase))
            fig.canvas.draw()
            fig.canvas.flush_events()
        # self.ir_fig, self.ir_ax = plt.subplots(figsize=(4, 4), facecolor='black')
        
        # # Returns a tuple of line objects, thus the comma
        # line1, = self.ir_ax.plot(self.time, self.ir_data, color='red', linewidth=2)
        # self.ir_ax.set_title("Temperature vs Time", fontsize=14, color='white', fontname='Courier')
        # self.ir_ax.set_xlabel("Time", fontsize=12, color='white', fontname='Courier')
        # self.ir_ax.set_ylabel("Temperature (°C)", fontsize=12, color='white', fontname='Courier')
        # self.ir_ax.set_facecolor('black')
        # self.ir_ax.spines['bottom'].set_color('white')
        # self.ir_ax.spines['top'].set_color('white')
        # self.ir_ax.spines['left'].set_color('white')
        # self.ir_ax.spines['right'].set_color('white')
        # self.ir_ax.tick_params(axis='x', colors='white')
        # self.ir_ax.tick_params(axis='y', colors='white')

        
        # # Embed graph in Tkinter
        # canvas = FigureCanvasTkAgg(self.ir_fig, master=frame)
        # canvas.draw()
        # canvas.get_tk_widget().pack(expand=True, fill="both")

        # line1.set_ydata([1,2,3,4,5,6])
        # canvas.draw()
        # canvas.flush_events()

    # Function to create the Ultrasonic Binary Graph
    def create_ultrasonic_graph(self, frame):
        fig, ax = plt.subplots(figsize=(4, 4), facecolor='black')
        ax.step(self.time, self.ultrasonic_data, color='cyan', linewidth=2, where='mid')  # Step plot for binary data
        ax.set_title("Ultrasonic Graph", fontsize=14, color='white', fontname='Courier')
        ax.set_xlabel("Time", fontsize=12, color='white', fontname='Courier')
        ax.set_ylabel("Binary Output (0 or 1)", fontsize=12, color='white', fontname='Courier')
        ax.set_facecolor('black')
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

        # Embed graph in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill="both")
    
    def add_ir_data(self):

        # Add the data to the classes data list
        self.ir_data.append(5)
        print(self.ir_data)
        self.time.append(runtime.time())
        
        self.create_ir_graph(self.ir_frame)

        self.root.after(1000, self.add_ir_data)






