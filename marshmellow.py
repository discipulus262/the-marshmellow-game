import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)
while True:
	if GPIO.input(2) == False:
		print("farshmellow makes a good input")
	time.sleep(0.5)
