# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

# Fan GPIO
FAN_GPIO = 18
# Low TEMP
MIN_TEMP = 48
# High TEMP
MAX_TEMP = 52
# How often to read CPU temperature in seconds
SAMPLING = 60

# Units in thousandths of a degree
def get_cpu_temp():
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        cpu_temp = int(f.read())
    return cpu_temp

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FAN_GPIO, GPIO.OUT)
    GPIO.output(FAN_GPIO, GPIO.LOW) 
    time.sleep(5)
    try:
        while 1:
            temp = get_cpu_temp()
            print('CPU temperature:', temp)
            if temp < MIN_TEMP * 1000:
                GPIO.output(FAN_GPIO, 0)
            elif temp > MAX_TEMP * 1000:
                GPIO.output(FAN_GPIO, 1)
            else:
                GPIO.output(FAN_GPIO, 1)
            time.sleep(SAMPLING)
    except KeyboardInterrupt:
        pass
    GPIO.cleanup()

if __name__ == '__main__':
    main()