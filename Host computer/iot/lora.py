import serial
import time
import re, json
from client import *
import queue

ser = serial.Serial("/dev/ttyUSB1",115200)
# lora_data = {"eid":"0","temperature":"0","humidity":"0","smokescope":"0","flame":"0"，"pressure":"0","wind":"0","direction":"0","misfile":"0","rain":"0"}
data_queue = queue.Queue()

def start_lora():
    while True:
        try:
            recv = ser.readline().decode('ascii')
            data = json.loads(recv)
            # data = eval(recv)
            data['eid'] = '设备' + data['eid']

            data_queue.put(data)
            
        except Exception as err:
            # print("lora", recv)
            print("lora", err)
            continue
        
        print(data)
    # return data
