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

##########DEBUG##########
# yRudder.ChangeDutyCycle(2)
# time.sleep(2)
# yRudder.ChangeDutyCycle(0)
# time.sleep(2)
# 
# for i in range(0,180,2):
# 	print i
# 	yRudder.ChangeDutyCycle(2 + i/18.00)
# 	time.sleep(0.03)
# 	yRudder.ChangeDutyCycle(0)
##########DEBUG##########

while(True):
	for i in range(0,180, 2):
		xRudder.ChangeDutyCycle(2 + i / 18.00)
 		yRudder.ChangeDutyCycle(2 + i / 18.00)
		time.sleep(0.03)
		#xRudder.ChangeDutyCycle(0)
		#yRudder.ChangeDutyCycle(0)
	 
	for i in range(180, 0, -2):
		xRudder.ChangeDutyCycle(2 + i / 18.00)
 		yRudder.ChangeDutyCycle(2 + i / 18.00)
		time.sleep(0.02)
		#xRudder.ChangeDutyCycle(0)
		#yRudder.ChangeDutyCycle(0)
