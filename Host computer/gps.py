import serial
import time
import re
import math

ser = serial.Serial("/dev/ttyUSB0",9600)
# ser.flushInput()
def getGPS():
    while True:
        try:
            recv = ser.readline().decode('gbk')
        except Exception as err:
            print(err)
            continue
            
        if recv.startswith('$GNRMC'):
            # print(recv)
            matchobj = re.search('A,.*?,N', recv,  re.M|re.I)
            N = matchobj.group(0)[2:-2]
            N = float(N)
            ND = N // 100
            NF = N % 100
            NM = math.modf(N)[0] * 60
            N = ND + NF / 60 + NM /3600
            N = '%.6f'%N
            
            matchobj = re.search('N,.*?,E', recv, re.M|re.I)
            E = matchobj.group(0)[2:-2]
            E = float(E)
            ED = E // 100
            EF = E % 100
            EM = math.modf(E)[0] * 60
            E = ED + EF / 60 + EM /3600 
            E = '%.6f'%E

            
            return N, E
                
if __name__ == '__main__':
    main()