import RPi.GPIO as GPIO
import time

CHANNEL = 36
GPIO.setmode(GPIO.BOARD)
GPIO.setup(CHANNEL,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)#have -> low vpuybai0

def getMQ2():
    status = GPIO.input(CHANNEL)
    # if status == True:
        # print("OK")
    # else:
        # print("smoking")
    return status   # 0-smoking
