import time
import math
import numpy as np
from multiprocessing import Process, Queue

from sc200reader import Sc200reader
from dosingpump_adafruit import Dosingpump
from ld20reader import LD20

class Calibrator:
    def __init__(self, target=None, conc1=None, conc2=None):

        self.target = target
        self.conc1 = conc1
        self.conc2 = conc2

        if ((self.target == 'ammonium') or (self.target == 'NH4')):

            print("Calibrating Ammonium")
            self.register = 40003

        elif ((self.target == 'nitrate') or (self.target == 'NO3')):

            print("Calibrating Nitrate")
            self.register = 40007

        else:
            self.register = None


    def calibrate(self):

        print("Calibration started")
        print("First dosage")
        measPoint1 = self.do_step()
        print("Second dosage")
        measPoint2 = self.do_step()

        [a, b] = np.polyfit(
                [measPoint1, measPoint2],
                [self.conc1, self.conc2],
                1
                )

        return a,b


    def do_step(self):

        ise = Sc200reader(14)
        ld20 = LD20()

        pump_time = 15
        #Measure flow through ld20 sensor as subrprocess
        qout = Queue()
        p = Process(target=ld20.get_volume, args=(qout,pump_time))
        p.start()
        # p.join()

        pump = Dosingpump()
        #Dose for 10 seconds
        pump.dose(pump_time,40)
        pump.cleanup()

        #Wait for 10 seconds
        time.sleep(2)

        volume = qout.get()

        print("Volume")
        print(volume)

        measList = []

        #Take 10 readings
        for i in range(10):
            measList.append(ise.read_float(self.register))
            time.sleep(0.5)

        #Take the mean of the readings
        measPoint = sum(measList)/len(measList)


        #Maybe check here for standard deviation, if too large, flush again and restart calibration

        print("Calibration point: " + str(measPoint))
        return measPoint

newCalibrator = Calibrator('ammonium', 10, 30)
a,b = newCalibrator.calibrate()

print(a,b)
