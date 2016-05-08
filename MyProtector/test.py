import RPi.GPIO as GPIO
import time
import signal
import atexit
 
atexit.register(GPIO.cleanup)	
GPIO.setmode(GPIO.BCM)
 
xPin = 21
GPIO.setup(xPin, GPIO.OUT, initial=False)
xRudder = GPIO.PWM(xPin, 50) #50HZ
xRudder.start(0)

yPin = 18
GPIO.setup(yPin, GPIO.OUT, initial=False)
yRudder = GPIO.PWM(yPin, 50) #50HZ
yRudder.start(0)

time.sleep(2)

# for i in range(0, 180, 3):
# 	x = round(float(i)/18, 2)
# 	yRudder.ChangeDutyCycle(x)
# 	time.sleep(0.01)
# 	print str(x)

yRudder.ChangeDutyCycle(0.01)
time.sleep(10)