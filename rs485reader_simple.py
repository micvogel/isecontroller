import minimalmodbus
import time


instrument = minimalmodbus.Instrument('/dev/ttyUSB_RS485_ICPCON',14)

successList = []


for i in range(17):
    
    print('Round: ' + str(i))
    
    try:
        nh4 = instrument.read_float(i, byteorder=0)
        print([i, nh4])
        successList.append([i, nh4])
        time.sleep(0.5)
        
    except:
        continue
        
        
print(successList)

# ser = serial.Serial('/dev/ttyUSB_RS485_ICPCON', 19200, timeout=1)
# print(ser)
# 
# ser.write(':010310010001EA\r\n')
# print(repr(ser.read(1000)))