import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN) #Input from sensor
GPIO.setup(17,GPIO.OUT) #Output pin that lights the LED

try:
    print " pir test"
    time.sleep(2) # Stabalize sensor
    print "Ready"
    while True:
       if GPIO.input(27):
		GPIO.output(17,1)# turns on LED
		time.sleep(1)
		GPIO.output(17,0)  # turns off LED)
		print("Motion Dectected...")
		time.sleep(1)
       time.sleep(1)


except KeyboardInterrupt:
	print "Quit"
	GPIO.cleanup()	

	
