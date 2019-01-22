#!/usr/bin/python
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)
blue = (0, 0, 255)

while(True):
	sense.show_message("HYDROBOTICS!!", text_colour=blue)
	break
