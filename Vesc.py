import pyvesc
from pyvesc import VESC
import time

# Notes
# - Not sure if we need to connect to the vesc everytime we run a command or if we can just connect once and then disconnect

# Create a VESC object with the appropriate serial port and baud rate
vesc = VESC("0", 115200)  # Replace "0" with the correct serial port
servo_vesc = VESC("0", 115200)  # Replace "0" with the correct serial port for the servo VESC

def move_forward(speed,t):
    vesc.connect()

    vesc.set_rpm(speed) #speed in rpm

    time.sleep(t) #how long it will move forward
    vesc.set_rpm(0)

def turn(servo_position,t):
    vesc.connect()
    servo_vesc.connect()

    vesc.set_rpm(speed) 
    servo_vesc.set_servo_pulsewidth(servo_position) 
    time.sleep(t) #how long it will turn for

    vesc.set_rpm(0)
    servo_vesc.set_servo_pulsewidth(0) 

def stop():
    vesc.connect()
    vesc.set_rpm(0) 



