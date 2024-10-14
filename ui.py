import tkinter as tk
from tkinter import LabelFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# Time data
time = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Temperature data (for IR Sensor Graph)
temperature = [10, 90, 30, 40, 20, 60, 50, 80, 90]

# Ultrasonic binary data (0s and 1s)
distance = [1, 0, 1, 1, 0, 1, 0, 0, 1]

# Function to create the IR Sensor Graph
def create_ir_graph(frame):
    fig, ax = plt.subplots(figsize=(4, 4), facecolor='black')
    ax.plot(time, temperature, color='red', linewidth=2)
    ax.set_title("Temperature vs Time", fontsize=14, color='white', fontname='Courier')
    ax.set_xlabel("Time", fontsize=12, color='white', fontname='Courier')
    ax.set_ylabel("Temperature (°C)", fontsize=12, color='white', fontname='Courier')
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

# Function to create the Ultrasonic Binary Graph
def create_ultrasonic_graph(frame):
    fig, ax = plt.subplots(figsize=(4, 4), facecolor='black')
    ax.step(time, distance, color='cyan', linewidth=2, where='mid')  # Step plot for binary data
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

# Create the main window
root = tk.Tk()
root.title("BUTM Intro Project Team One")

# Set the window size (use "geometry" if you want fixed starting size)
root.geometry("800x600")
root.configure(bg="black")  # Set background to black

# Set grid weight for responsiveness
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)

# Create the title label
title_label = tk.Label(root, text="BUTM INTRO PROJECT TEAM ONE", font=("Courier", 24), bg="black", fg="#55ACEE")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Create the left IR Sensor graph section
ir_frame = LabelFrame(root, text="IR Sensor Graph", font=("Courier", 16), fg="white", bg="black", bd=5, labelanchor="n")
ir_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")  # Grid makes the layout responsive

# Create the right Ultrasonic Sensor graph section
ultrasonic_frame = LabelFrame(root, text="Ultrasonic Graph", font=("Courier", 16), fg="white", bg="black", bd=5, labelanchor="n")
ultrasonic_frame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

# Create and display the graphs in the respective sections
create_ir_graph(ir_frame)
create_ultrasonic_graph(ultrasonic_frame)

# Run the Tkinter event loop
root.mainloop()
