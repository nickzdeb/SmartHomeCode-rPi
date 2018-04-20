import RPi.GPIO as GPIO
import time
import datetime

now = datetime.datetime.now()

#GPIO.setmode(GPIO.BCM)

#pin_to_circuit0 = 2 #Left
#pin_to_circuit1 = 26 #Right
#pin_to_circuit2 = 19

#GPIO.setup(pin_to_circuit0, GPIO.IN)
#GPIO.setup(pin_to_circuit1, GPIO.IN)
#GPIO.setup(pin_to_circuit2, GPIO.OUT)

#GPIO.setwarnings(False)

#while(True):
#GPIO.output(pin_to_circuit0, GPIO.HIGH)
    #time.sleep(1)
    #GPIO.output(pin_to_circuit0, GPIO.LOW)

    #a = float(GPIO.input(pin_to_circuit0))
    #print(a)
    #b = float(GPIO.input(pin_to_circuit1))
    #print(b)
    #time.sleep(1)

#GPIO.setup(pin_to_circuit1, GPIO.IN)


#GPIO.output(pin_to_circuit2, GPIO.HIGH)
    #time.sleep(1)
    #GPIO.output(pin_to_circuit2, GPIO.LOW)


print(now)
