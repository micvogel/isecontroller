import minimalmodbus
import time


class Sc200reader:
    
    def __init__(self, address=None, byteorder=0):
       self.address = address
       self.byteorder = byteorder
        
       self.instrument = minimalmodbus.Instrument(
             '/dev/ttyUSB_RS485_ICPCON',address)
    
       self.floatList = [
            40001, 40003, 40005, 40007, 40009, 400011, 40013, 40015,
            40036, 40038, 40043, 40046, 40055, 40057, 40063, 40065, 
            40067, 40069, 40071, 40073, 40075, 40077, 40079, 40081,
            40083, 40085, 40087, 40089, 40091, 40093, 40097, 40099,
            40121, 40125, 40129, 40133, 40137, 40141, 40145, 40149,
            40175, 40177, 40181, 40183, 40187
            ]

    
    def read_float(self, register_raw):
       """This function converts the register address in the manual to
       a decimal register and reads this register from the ISE.
      
       return result: asked value, if not availabe, return 999999
       rtype: float
       """
       register_dec = register_raw - 40001
        
       if register_raw in self.floatList:
          result = self.instrument.read_float(
                register_dec, 
                byteorder=self.byteorder
                )
       else:
          print("The register is not valid. Possible reason: Register"
             + " is not integrated in the Sc200reader class or is not on"
             + " register list in the manual")
          result = 999999
            
       return round(result,2)

        

    

