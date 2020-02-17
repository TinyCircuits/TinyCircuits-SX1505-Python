# Joystick Wireling Example
# This example will print out the direction the Joystick is toggled
# Note: The "up" direction is the one closest to the 5-pin connector
# Written by: Laverena Wienclaw for TinyCircuits

import tinycircuits_sx1505
import tinycircuits_wireling
import time

wireling = tinycircuits_wireling.Wireling()
wireling.selectPort(0)

joystick = tinycircuits_sx1505.SX1505()

while True:
    joystick.getJoystickPos()
    if(joystick.up):
        print("up")
    elif(joystick.down):
        print("down")
    elif(joystick.left):
        print("left")
    elif(joystick.right):
        print("right")
    time.sleep(.1)
