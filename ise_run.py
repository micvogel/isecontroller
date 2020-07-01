from sc200reader import Sc200reader
import time

ise = Sc200reader(address=14)



for i in range(100):
    time.sleep(0.5)
    print(ise.read_register(40013))
    