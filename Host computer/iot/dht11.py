import Adafruit_DHT

sensor1 = Adafruit_DHT.DHT11

def getDht11():
    humidity1, temperature1 = Adafruit_DHT.read_retry(sensor1, 4)#4 是 GPIO4
    return humidity1, temperature1
#print(humidity1,temperature1)