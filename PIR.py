import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#pin_to_circuit0 = 3
pin_to_circuit1 = 4
#pin_to_circuit2 = 19


GPIO.setup(pin_to_circuit1, GPIO.IN)

GPIO.setwarnings(False)

#while(True):
#GPIO.output(pin_to_circuit0, GPIO.HIGH)
    #time.sleep(1)
    #GPIO.output(pin_to_circuit0, GPIO.LOW)

#GPIO.output(pin_to_circuit1, GPIO.HIGH)
#time.sleep(10)

while True
    a = float(GPIO.input(pin_to_circuit1))
    print(a)

#GPIO.setup(pin_to_circuit1, GPIO.IN)


#GPIO.output(pin_to_circuit2, GPIO.HIGH)
    #time.sleep(1)
    #GPIO.output(pin_to_circuit2, GPIO.LOW)


