from struct import *
import serial

ser = serial.Serial("COM3", 115200)

def pacemaker_serial_comm(parametersList):
    print(parametersList)
    print(parametersList[13])

    activity_threshold = {"V-Low":2, "Low":8, "Med-Low":14, "Med":20, "Med-High":26, "High":32, "V-High":38 }

    if (parametersList[14]!=0):
        parametersList[14] = activity_threshold.get(parametersList[14])

    print("VALUE IS", parametersList[10])
    parametersList[4] = int(parametersList[4]*10)
    parametersList[5] = int(parametersList[5]*10)
    parametersList[6] = int(parametersList[6]*10)
    parametersList[7] = int(parametersList[7]*10)
    parametersList[10] = int(float(parametersList[13]))*10
    parametersList[11] = int(parametersList[11])*10
    parametersList[12] = int(parametersList[12])*10
    parametersList[13] = int(float(parametersList[13]))*10
    print(parametersList[13])
    parametersList[15] = int(float(parametersList[15]))*10
    parametersList[16] = int(float(parametersList[16]))*10
    parametersList[17] = int(float(parametersList[17]))*10

    print(parametersList)

    packingPattern = "<HHHHHHHHHHHHHHHHHHHHH"
    #packingPattern = "<??BBffdd??ffBBBBBH?BB"
    endian = packingPattern[0]
    packingPattern = packingPattern[1:]
    
    packetList = []
    
    for i in range(0, len(parametersList)):
        print(parametersList[i])
        packedData = pack((endian + packingPattern[i]), parametersList[i])
        packetList.append(packedData)
    
    for packet in packetList:
        ser.write(packet)

######################### OLDER CODE #####################################

#import serial
##from graphing import *

#def pacemaker_serial_comm(parametersList):
#	pacemaker_inputs = parametersList

#	#try: 
#	ser = serial.Serial("COM3", 115200, bytesize=serial.SEVENBITS, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_EVEN, timeout=1) 
#	ser.close()
#	ser.open() 
#	#ser.write(bytearray(pacemaker_inputs))
#	print(pacemaker_inputs)

#	#except(serial.SerialException):
#	#	print("Device cannot be found or cannot be configured.")

#if __name__ == '__main__':
#	paraList = [1,2,3,4,5]
#	#pacemaker_serial_comm(paraList)