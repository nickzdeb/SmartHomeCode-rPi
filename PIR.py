import RPi.GPIO as GPIO
import time

import pymongo
from pymongo import MongoClient
client = MongoClient('mongodb://admin:admin@ds237979.mlab.com:37979/apollo-dev')
db=client['apollo-dev']

GPIO.setmode(GPIO.BCM)

pin_to_circuit1 = 9

GPIO.setup(pin_to_circuit1, GPIO.IN)

GPIO.setwarnings(False)

while(True):
    time.sleep(2)
    a = float(GPIO.input(pin_to_circuit1))
    print(a)

#Store in database 
data={"uuid": "1", "motion": bool(a)}
result=db.temp_hum.insert(data)



