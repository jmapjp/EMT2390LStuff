#Servos often 'respond' to a wider range than 1.0-2.0 milliseconds so try it with ranges of 50 (0.5ms) to 250 (2.5ms)

#Of course you can try any number between 50 and 250! so you get a range of about 200 positions

#Note that the Raspberry Pi PWM is not necessarily a 'stable' output, and there might be some jitter! For 
import time
import wiringpi
 
# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()
 
# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
 
# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
 
# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)
 
delay_period = 0.01
 
while True:
        for pulse in range(50, 250, 1):
                wiringpi.pwmWrite(18, pulse)
                time.sleep(delay_period)
        for pulse in range(250, 50, -1):
                wiringpi.pwmWrite(18, pulse)
                time.sleep(delay_period)
