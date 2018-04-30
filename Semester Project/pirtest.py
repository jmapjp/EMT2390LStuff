#Read Now, we can try reading the output from the PIR motion sensor. The sensor outputs a digital HIGH (5V) signal when it detects #a person. Copy and paste the following code into your Raspberry Pi and save it as a Python file.

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin
while True:
i=GPIO.input(11)
if i==0:                 #When output from motion sensor is LOW
print "No intruders",i
GPIO.output(3, 0)  #Turn OFF LED
time.sleep(0.1)
elif i==1:               #When output from motion sensor is HIGH
print "Intruder detected",i
GPIO.output(3, 1)  #Turn ON LED
time.sleep(0.1)
