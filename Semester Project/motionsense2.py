import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.IN) #Input from sensor
GPIO.setup(7,GPIO.OUT) #Output pin that lights the LED

sensemode = GPIO.input(5)
while True:
	if sensemode == 0:
		print " No one is near", sensemode 
		GPIO.output(7,0)  # turns off LED
		time.sleep(0.5)
	
	elif sensemode == 1:
		print " Someone is here" , sensemode
		GPIO.output(7,1)  # turns on LED 
		time.sleep(0.5)

	
