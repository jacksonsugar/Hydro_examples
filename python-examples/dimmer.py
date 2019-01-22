import time
import RPi.GPIO as GPIO #Import Rpi Library for GPIO pin control
GPIO.setmode(GPIO.BOARD) #Using physical pin number scheme
GPIO.setwarnings(False)

LED1=12                  #LED1 is on pin 12

GPIO.setup(LED1,GPIO.OUT)  #led is output
pwm=GPIO.PWM(LED1,100)     #Initialize pwm 100Hz frequency
dc=0  			   #duty cycle
pwm.start(dc)  		   #start pwm with 0% duty cycle

while True:
	for dc in range(0, 101, 5): #Loop from 0 to 100 by increments of 5
		pwm.ChangeDutyCycle(dc)
		time.sleep(0.1)
	for dc in range(95, 0, -5): #Loop from 95 to 5 by decreasing by 5
		pwm.ChangeDutyCycle(dc)
		time.sleep(0.1)

