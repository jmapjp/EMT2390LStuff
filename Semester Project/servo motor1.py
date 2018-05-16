#The following program will control the servo making it move to its neutral position (90 degrees), wait 1 second and then move to its 0 degrees, wait 1 second and finally move to its 180 degrees. The cycle continues until interrupted:

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(15, GPIO.OUT)

p = GPIO.PWM(15, 50)

p.start(7.5)

try:
        while True:
		p.ChangeDutyCycle(88.8)  # turn towards 90 degree
		time.sleep(1) # sleep 1 second
		p.ChangeDutyCycle(20.5)  # turn towards 0 degree
		time.sleep(1) # sleep 1 second
		p.ChangeDutyCycle(100) # turn towards 180 degree
                time.sleep(1) # sleep 1 second 

except KeyboardInterrupt:
	p.stop()
        GPIO.cleanup()
