import RPi.GPIO as GPIO  
import time  
import signal  
import atexit  



atexit.register(GPIO.cleanup)    

servopin = 40  
GPIO.setmode(GPIO.BOARD)  
GPIO.setup(servopin, GPIO.OUT, initial=False)  
p = GPIO.PWM(servopin,50) #50HZ  
p.start(0)  
time.sleep(2)  

def pwm_():
    while(True):  
        for i in range(0,181,5):  
            p.ChangeDutyCycle(1 + 5 * i / 90) #设置转动角度  
            time.sleep(0.02)                      #等该20ms周期结束  
            p.ChangeDutyCycle(0)                  #归零信号  
            time.sleep(0.15)  

        for i in range(181,0,-5):  
            p.ChangeDutyCycle(1 + 5 * i / 90)  
            time.sleep(0.02)  
            p.ChangeDutyCycle(0)  
            time.sleep(0.15)  
