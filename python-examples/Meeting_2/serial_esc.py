import RPi.GPIO as GPIO
import time
import serial
from numpy import interp #for interpolation between potentiometer and servo

escpin=12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(escpin,GPIO.OUT)
pwm=GPIO.PWM(escpin,50) #pwm with frequency of 50 Hz
pwm.start(7.5) #servo starts at center
print 'Centering Servo'
time.sleep(3)

ser= serial.Serial(
	port='/dev/serial0', #serial port the object should read
	baudrate= 9600,      #rate at which information is transfered over comm channel
	parity=serial.PARITY_NONE, #no parity checking
	stopbits=serial.STOPBITS_ONE, #pattern of bits to expect which indicates the end of a character
	bytesize=serial.EIGHTBITS, #number of data bits
	timeout=1
)

while 1:
	read = ser.readline() #reads value from potentiometer
	print read    #debug line for help
	read = float(read)   #turns the serial char to numbers
	dc = interp(read,[0,1023],[11,19]) #interpolate potentiometer values to servo values
	pwm.ChangeDutyCycle(dc) #servo moves with potentiometer input
	time.sleep(.1)
