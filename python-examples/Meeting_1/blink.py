import time
import RPi.GPIO as GPIO #Import Rpi Library for GPIO pin control
GPIO.setwarnings(False) #So the computer doesn't scream at you
GPIO.setmode(GPIO.BOARD) #Using physical pin number scheme
GPIO.setup(12,GPIO.OUT,initial=GPIO.LOW) #set initial value to low, led pin 12

while True:
	GPIO.output(12,GPIO.HIGH) #led ON
	time.sleep(1)             #sleep for 1 second
	GPIO.output(12,GPIO.LOW)  #led OFF
	time.sleep(1)             #sleep for 1 second
