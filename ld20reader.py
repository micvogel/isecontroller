"""
@Authour: Michael Vogel
Date: 2020-07-07
"""


# Modules
import smbus
import time
import numpy as np
import scipy

class LD20:
    def __init__(self):
        
        # LD20 hex adres
        self.address     = 0x08
        self.LD20_SS       = 0x36
        self.LD20_HIGH     = 0x06
        self.LD20_READ     = 0x00
        
        self.bus = smbus.SMBus(1)
        self.bus.write_i2c_block_data(self.address,0x3F, [0xF9])

        # MS to SL
        self.bus.write_i2c_block_data(self.address,0x36, [0x08])
        time.sleep(0.2)  
  
    def get_volume(self, meastime=10):
        """This function reads flow from ld20 sensor
        via i2c and returns it.
        return: flow
        rtype: float

        """
        measstep = 1
        
        times = []
        flows = []
               
        start_time = time.time()       

        meascheck = 1
        while meascheck:
            # Read out data
            data = self.bus.read_i2c_block_data(self.address,self.LD20_READ,6)

            # Devide data into counts flow
            f_data = data[0] << 8 | data[1]

            # Convert counts to Temperature/Humidity and round on two decimals
            flow = round(np.float(f_data)/20/3600,2)
            timeellapsed = round(time.time() - start_time, 2)
            times.append(timeellapsed)
            flows.append(flow)
      
            print(str(timeellapsed) + ' -> ' + str(flow))
      
            if timeellapsed > meastime:
                meascheck = 0
            else:
                time.sleep(measstep)
            

        volume = round(np.trapz(flows, times),2)
        print('Volume: ' + str(volume))
        self.bus.write_i2c_block_data(self.address,0x3F, [0xF9])
        # Return Temperature and Humdity
        return flow
    
new_ld20 = LD20()
print(new_ld20.get_volume(40))