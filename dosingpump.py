"""
2.5 -> 0° -> Clockwise maximum speed rotation
7.5 -> 90° -> Stop
12.5 -> 180° -> Counterclockwise maximum speed rotation
"""

import RPi.GPIO as GPIO
import time

class Dosingpump:
    
    def __init__(self): 
        self.pumpPin = 27
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pumpPin, GPIO.OUT)
        
        self.p = GPIO.PWM(self.pumpPin, 500)
        self.p.start(2.5)
        
        
    def start(self):
        for i in range(5):
            self.p.ChangeDutyCycle(2.5)
            time.sleep(1)
            self.p.ChangeDutyCycle(7.5)
            time.sleep(1)
            self.p.ChangeDutyCycle(12.5)
            time.sleep(1)
            self.p.ChangeDutyCycle(7.5)
            time.sleep(1)
            self.p.ChangeDutyCycle(2.5)
                
        self.p.stop()
        GPIO.cleanup()

            