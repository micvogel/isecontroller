import serial
import time
import serial.rs485

def transmit_byte(b):
   print(str(b) + ' ' + str(ord(b)))
   ser.write(b)
   time.sleep(0.00003)
   
def transmit_command(cmd):
    for i in range(len(cmd)):
        transmit_byte(cmd[i:i+1])
        
ser = serial.rs485.RS485(
    port = '/dev/ttyUSB_RS485_ICPCON',
    baudrate = 19200,
    timeout = 1    
    )

address = 0x02
cmd = b'$' + bytes(hex(address)[2:4], 'utf-8') + b'32/r'
print(cmd)
transmit_command(cmd)

response = ser.readline();
print(response)

# for c in range(20):
#     for onoff in range(2):
#         for nr in range(8):
#             cmd = (
#                 b'#' + bytes(hex(address)[2:4], 'utf-8') +
#                 b'0' + bytes(str(onoff), 'utf-8') + b'\r'
#                 )
#             print(cmd)
#             transmit_command(cmd)
#             time.sleep(0.2)
#             
