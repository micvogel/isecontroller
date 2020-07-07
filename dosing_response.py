import time

from dosingpump_adafruit import Dosingpump

new_dosingpump = Dosingpump()

print("Start in: ")

for i in range(5):
    print(5-i)
    time.sleep(1)
    
#Dose 8 ml
new_dosingpump.dose(30,40)
time.sleep(10)
#Dose 10 ml
# new_dosingpump.dose(10,5)





print("Time is over")

new_dosingpump.cleanup