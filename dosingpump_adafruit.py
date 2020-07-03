import RPi.GPIO as GPIO
import time

class Dosingpump:
    
    def __init__(self): 
        self.pumpPin = 18
        self.pumpPin2 = 23
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pumpPin2, GPIO.OUT)
        GPIO.setup(self.pumpPin, GPIO.OUT)
        
        self.p = GPIO.PWM(self.pumpPin, 50)
        self.p.start(0)
        
        
    def dose(self,pumptime=10,dc=100):
        self.p.ChangeDutyCycle(dc)
        GPIO.output(self.pumpPin2, GPIO.HIGH)
        time.sleep(pumptime)
        GPIO.output(self.pumpPin2, GPIO.LOW)
        self.p.ChangeDutyCycle(0)


    def cleanup(self):
        self.p.stop()
        GPIO.cleanup()
        
