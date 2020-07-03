from sc200reader import Sc200reader
import time

ise = Sc200reader(address=14)



for i in range(1):
    time.sleep(0.5)
    print(i + 100)
    try:
        print(ise.write(40121))
    except Exception as e:
        print(e)
    
