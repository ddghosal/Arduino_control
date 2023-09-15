import time
from pyfirmata import Arduino, util
print("L3")
# Define the port where your Arduino is connected
port = '/dev/cu.usbmodem14101'  #'COM12'  # to be replaced with the appropriate port on the system: COMxx for windows
print('L6')
# Create an Arduino board object
board = Arduino(port)
print('L9')
# Set the digital pin numbers for the DMD signal, machine trigger pulse, and camera trigger
dmd_signal_pin = 2  # Replace with the actual DMD signal pin
machine_trigger_pin = 3  # Replace with the actual machine trigger pulse pin
camera_trigger_pin = 4  # Replace with the camera trigger pin
print('L14')
# Set the digital pin modes
board.digital[dmd_signal_pin].mode = 0  # DMD signal pin as INPUT
board.digital[machine_trigger_pin].mode = 0  # Machine trigger pulse pin as INPUT
board.digital[camera_trigger_pin].mode = 1  # Camera trigger pin as OUTPUT
print('L19')
# Function to trigger the camera
def trigger_camera():
    board.digital[camera_trigger_pin].write(1)  # Send a high signal to trigger the camera
    time.sleep(0.1)  # Keep the signal high for a short duration (adjust as needed)
    board.digital[camera_trigger_pin].write(0)  # Send a low signal to the camera
print('L25')
# Create a Firmata iterator to listen for incoming signals
it = util.Iterator(board)
it.start()
print('L29')
try:
    while True:
        # Read the status of the DMD signal and machine trigger pulse
        dmd_signal_status = board.digital[dmd_signal_pin].read()
        machine_trigger_status = board.digital[machine_trigger_pin].read()

        # Check if both DMD signal and machine trigger pulse are HIGH (active)
        if dmd_signal_status == 1 and machine_trigger_status == 1:
            print("Received DMD signal and machine trigger pulse. Triggering the camera.")
            trigger_camera()
        else:
            print("camera not triggered!")
        
        time.sleep(0.1)  # Adjust the sleep duration as needed
    print('L44')        
except KeyboardInterrupt:
    board.exit()  # Close the Arduino connection when the script is interrupted
