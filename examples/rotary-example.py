# Rotary Wireling Example
# This example will print out the numbered direction the Rotary is toggled
# Written by: Laverena Wienclaw for TinyCircuits

import tinycircuits_sx1505
import tinycircuits_wireling
import time

wireling = tinycircuits_wireling.Wireling()
wireling.selectPort(0)

rotary = tinycircuits_sx1505.SX1505()

while True:
    position = rotary.getRotaryPos()
    print("Number direction: {}".format(position)) 
    time.sleep(.5)
