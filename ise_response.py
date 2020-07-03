import time
import matplotlib.pyplot as plt
import time
import math
import numpy as np

from sc200reader import Sc200reader



ise = Sc200reader(14)

register = 40003
        
file = open("data.txt", "w")

times = []
measList = []
       
start_time = time.time()        

try: 
    while True:
        conc = ise.read_float(register)

        timeEllapsed = round(time.time() - start_time, 2)
        
        print("Time [s]: " + str(timeEllapsed))
        print("NH4 [mg/l] : " + str(conc))
        
        times.append(timeEllapsed)
        measList.append(conc)
        
        datastr = str(timeEllapsed) + ";" + str(conc) + "\n"
        
        file.write(datastr)
        
        time.sleep(0.48)    
    
except Exception as e:
    print(Exception)

except KeyboardInterrupt:
    
   
    file.close()
    
    fig, ax = plt.subplots()
   
    ax.set_xlabel("time [s]")
    ax.set_ylabel("NH4 [mg/l]", color='red')
    ax.plot(times, measList, label="NH4", color='red')
    
    ax.grid()

    plt.show()
