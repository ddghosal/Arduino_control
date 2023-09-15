from Arduino import Arduino
import time
import serial
from serial import *

# Define the serial port where your Arduino is connected
port = '/dev/cu.usbmodem14101'  # Replace with the appropriate port on the  system
baud_rate = 57600  # Match the baud rate in Arduino sketch, could be 9600 or so..

# Create an Arduino board object
board = Arduino(port)

# Open the serial connection to the Arduino
ser = serial.Serial(port, baud_rate)

# Define the pin numbers for the DMD signal, machine trigger pulse, and camera trigger
dmd_signal_pin = 7  # modify in accordance with the right DMD signal pin
machine_trigger_pin = 8  # modify in accordanc with the right machine trigger pulse pin
camera_trigger_pin = 9  # modify in accordanc with the right camera trigger pin


# Set the digital pin mode to OUTPUT
board.digital[camera_trigger_pin].mode = 1  # Input(mode 0), while Output(mode 1)

# Function to trigger the camera
def trigger_camera():
    print("Triggering the camera")
    # Implement camera trigger code here
    board.digital[camera_trigger_pin].write(1)  # Send a high signal (5V)
    time.sleep(0.1)  # Keep the signal high for a short duration (adjust as needed)
    board.digital[camera_trigger_pin].write(0)  # Send a low signal (0V)

try:
    while True:
        # Read the status of the DMD signal and machine trigger pulse
        dmd_signal_status = ser.read(1)
        machine_trigger_status = ser.read(1)

        # Check if both DMD signal and machine trigger pulse are HIGH (active)
        if dmd_signal_status == b'1' and machine_trigger_status == b'1':
            print("Received DMD signal and machine trigger pulse. Triggering the camera.")
            # Trigger the camera by setting the camera trigger pin HIGH
            ser.write(b'1')  # Send '1' to the Arduino for camera trigger as byte type
            trigger_camera()  # Implement camera-specific logic
            ser.write(b'0')  # Set the camera trigger pin LOW
            
        time.sleep(0.1)  # Adjust the sleep duration as needed
except KeyboardInterrupt:
    ser.close()  # Close the serial connection when the script is interrupted
