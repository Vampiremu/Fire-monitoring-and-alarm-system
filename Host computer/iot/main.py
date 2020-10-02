import threading
import time
from dht11 import *
from mq_2 import *
from gps import *
from client import *
from lora import *
from pwm import *
from bme280_2 import *

data = {
    "eid": "设备1",
    "temperature": "25",    
    "humidity": "30",
    "smokescope": "45",
    "flame": "30",
    "pressure": "23",
    "wind": "90",
    "direction": "东风",
    "misfile": "否",
    "rain": "否"
    }

h, t = 0, 0
mq2 = 0
n, e = 0, 0

def thread_dht11():
    global h, t

    while True:
        h, t = getDht11()

def thread_mq2():
    global mq2

    while True:
        mq2 = getMQ2()
    
def thread_gps():
    global n, e

    while True:
        n, e = getGPS()

def theard_bme280():
    global p

    while True:
        p = bme280_()

def thread_send():
    s = SendData()

    while True:
        data = data_queue.get()
        s.SetGeturlID(data['eid'])
        if not s.send(data):
            print('main ERROR')
        
        print(s.http_get())

def therad_pwm():
    while True:
        pwm_()

def main():
    t_dht11 = threading.Thread(target=thread_dht11)
    t_mq2 = threading.Thread(target=thread_mq2)
    t_gps = threading.Thread(target=thread_gps)
    t_lora = threading.Thread(target=start_lora)
    t_send = threading.Thread(target=thread_send)
    t_pwm = threading.Thread(target=therad_pwm)
    t_bme280 = threading.Thread(target=theard_bme280)
    
    t_dht11.setDaemon(True)
    t_mq2.setDaemon(True)
    t_gps.setDaemon(True)
    t_lora.setDaemon(True)
    t_send.setDaemon(True)
    t_pwm.setDaemon(True)
    t_bme280.setDaemon(True)

    t_dht11.start()
    t_mq2.start()
    t_gps.start()
    t_lora.start()
    t_send.start()
    t_pwm.start()
    t_bme280.start()

    while True:
        print(h, t, mq2, p, n, e)
        data['temperature'] = str(t)
        data['humidity'] = str(h)
        data['smokescope'] = str(mq2)
        data['pressure'] = str(p)
        data['wind'] = str(n)   #纬度
        data['direction'] = str(e)  #经度
        
        data_queue.put(data)
        

        time.sleep(1)
    
if __name__ == '__main__':
    main()