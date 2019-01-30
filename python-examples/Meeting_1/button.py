import time
import RPi.GPIO as GPIO #Import Rpi Library for GPIO pin control
GPIO.setmode(GPIO.BOARD) #Using physical pin number scheme
GPIO.setwarnings(False)
LED1=12                  #LED1 is on pin 12
button=36                #Button is on pin 36
GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP)  #button is input
GPIO.setup(LED1,GPIO.OUT)   			     #led is output
while True:
        button_state=GPIO.input(button)
	if button_state==False:
		GPIO.output(LED1,GPIO.HIGH) #led on
		time.sleep(0.1)             #sleep for 0.1 secs
	else:
		GPIO.output(LED1,GPIO.LOW)  #led off
		time.sleep(0.1)             #sleep for 0.1 secs
	time.sleep(.1)                           
