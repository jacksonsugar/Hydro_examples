import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
servopin=12
GPIO.setup(servopin,GPIO.OUT)

pwm=GPIO.PWM(servopin,50)
dc=11
pwm.start(dc) #dc goes from 1 to 20

time.sleep(1)

while True:
	pwm.ChangeDutyCycle(2.5)
	time.sleep(1)
	pwm.ChangeDutyCycle(7.5)
	time.sleep(1)
	pwm.ChangeDutyCycle(12.5)
	time.sleep(1)
