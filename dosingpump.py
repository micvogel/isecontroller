import RPi.GPIO as GPIO
import time

class Dosingpump:
    
    def __init__(self): 
        self.pumpPin = 18
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pumpPin, GPIO.OUT)
        
        self.p = GPIO.PWM(self.pumpPin, 50)
        self.p.start(0)
        
        
    def dose(self,pumptime,dc=100):
        self.p.ChangeDutyCycle(dc)
        time.sleep(pumptime)
        self.p.ChangeDutyCycle(0)


    def cleanup(self):
        self.p.stop()
        GPIO.cleanup()
        


            