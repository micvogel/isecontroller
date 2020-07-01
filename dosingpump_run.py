import RPi.GPIO as GPIO
import time


pumpPin = 22
        
GPIO.setmode(GPIO.BCM)
GPIO.setup(pumpPin, GPIO.OUT)
        
p = GPIO.PWM(pumpPin, 500)
p.start(2.5)
        
print("Start")
time.sleep(3)
print("Stop")
p.ChangeDutyCycle(7.5)
time.sleep(3)
print("Pump start")
p.ChangeDutyCycle(2.5)
time.sleep(12.5)
p.ChangeDutyCycle(7.5)
print("Stop")

p.stop()
GPIO.cleanup()