import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #Sets pin number mode
GPIO.setup(11,GPIO.OUT) #Output pin that lights the LED
GPIO.setup(13,GPIO.IN) #Input from sensor1
GPIO.setup(19,GPIO.OUT)# Output that lights LEd #2
GPIO.setup(21,GPIO.IN)#Input from Sensor #2
GPIO.setup(15,GPIO.OUT)# Pin to send signal to servo
p = GPIO.PWM(15, 50)
p.start(7.5)
try:
    print " pir with motor"
    time.sleep(2) # Stabalize sensor
    print "Ready"
   
    while True:
	if GPIO.input(13): # if motion sensor 1 is high
		
        	GPIO.output(11,1)   #Outputs digital HIGH signal (5V) on pin 11
        	p.ChangeDutyCycle(10)  # turn towards 90 degree
		print "Motion Detected on sensor 1"
		time.sleep(2)      #Time delay of 1 second
		GPIO.output(11,0) # Outputs Low signal on pin 11 tunring led1 off

        elif GPIO.input(21):    # Or if motion sensor 2 is high
                GPIO.output(19,1)       # Turns on ED 2 via high output signal
                p.ChangeDutyCycle(5)   # Turns motor
		print "Motion Detected on sensor 2"
		time.sleep(2)
                GPIO.output(19,0)       #Outputs digital LOW signal (0V) on pin 19
	        time.sleep(1)
	time.sleep(1)


except KeyboardInterrupt:
        p.stop()
	print " DEMO END"
        GPIO.cleanup()
