import RPi.GPIO as GPIO
import time
import datetime

now = datetime.datetime.now()

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

ss_relay_1 = 17 #solid state relay pin 1
GPIO.setup(ss_relay_1, GPIO.OUT)

#while(True):
    #GPIO.output(ss_relay_1, GPIO.HIGH)
    #time.sleep(3)
GPIO.output(ss_relay_1, GPIO.HIGH)
    #time.sleep(3)

#pin_to_circuit0 = 14 #Left
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
    #print("Left: ", a)
    #b = float(GPIO.input(pin_to_circuit1))
    #print("Right: ", b)
    #time.sleep(1)

#GPIO.setup(pin_to_circuit1, GPIO.IN)


#GPIO.output(pin_to_circuit2, GPIO.HIGH)
    #time.sleep(1)
    #GPIO.output(pin_to_circuit2, GPIO.LOW)


#print(now)
