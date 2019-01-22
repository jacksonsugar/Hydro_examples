import os
import time

#Use os.system to execute other scripts and wait to continute

try:
	os.system('python blink.py') #run blink script

except KeyboardInterrupt: #keyboard interrupt stops script 
	time.sleep(1)

print('Moving on!')

time.sleep(1)

os.chdir('/home/pi/Documents/Hydro_examples/python-examples/files/cats/') #change directory

os.system('cp meow.txt purrrr.txt') #make new file called purrrr from meow.txt

time.sleep(1)

print 'Listing Files in files directory...'

files = os.listdir('/home/pi/Documents/Hydro_examples/python-examples/files/') #list directory

print files
