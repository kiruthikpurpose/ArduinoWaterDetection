import serial
import tkinter as tk

# Initialize serial communication with Arduino
ser = serial.Serial('COM7', 9600)  # Update 'COM3' with your Arduino's serial port

# Function to read distance data from serial port and update GUI
def update_gui():
    # Read distance data from serial port
    distance_str = ser.readline().decode().strip()
    distance = int(distance_str)
    
    # Update GUI
    canvas.delete("all")
    canvas.create_rectangle(50, 200 - distance * 2, 100, 200, fill="blue")
    root.after(100, update_gui)  # Update GUI every 100 milliseconds

# Create GUI
root = tk.Tk()
root.title("Water Tank Level")
canvas = tk.Canvas(root, width=150, height=200)
canvas.pack()

# Start updating GUI
update_gui()

root.mainloop()
