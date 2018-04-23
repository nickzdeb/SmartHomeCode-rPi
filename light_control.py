import time
import RPi.GPIO as GPIO
import datetime
import pymongo

from pymongo import MongoClient
client = MongoClient('mongodb://admin:admin@ds237979.mlab.com:37979/apollo-dev')
db=client['apollo-dev']

now = datetime.datetime.now()

GPIO.setmode(GPIO.BCM)             # Set GPIO output pins format
GPIO.setwarnings(False)

switch1_isOn = False
switch2_isOn = False

touch_input_left = 2 #touch input pin 1
GPIO.setup(touch_input_left, GPIO.IN) 

touch_input_right = 26 #touch input pin 2
GPIO.setup(touch_input_right, GPIO.IN)


ss_relay_1 = 17 #solid state relay pin 1
GPIO.setup(ss_relay_1, GPIO.OUT) 

ss_relay_2 = 27 #solid state relay pin 2
GPIO.setup(ss_relay_2, GPIO.OUT) 

while(True):
    #Switch 1
    try:
        switch1 = db.light_control_1.find().sort('_created_at',-1).limit(1)
        for object in switch1:
            print ("light control 1 ", object["signal"])
            switch1_isOn = object["signal"]
    except Exception, e:
        print str(e)

    #Switch 2
    try:
        switch2 = db.light_control_2.find().sort('_created_at',-1).limit(1)
        for object in switch2:
            print ("light control 2 ", object["signal"])
            switch2_isOn = object["signal"]
    except Exception, e:
        print str(e)

    #Assume SSR's are off


    if switch1_isOn == True:
        GPIO.output(ss_relay_1, GPIO.HIGH)
    else:
        GPIO.output(ss_relay_1, GPIO.LOW)
    
    if switch2_isOn == True:
        GPIO.output(ss_relay_2, GPIO.HIGH)
    else:
        GPIO.output(ss_relay_2, GPIO.LOW)
    time.sleep(2)


#Store in database
#data={"uuid": "1", "entry_num": 5, "lighting": answer, "day": now.day, "time": str(now.hour)+":"+str(now.minute)}
#result=db.light_control.insert(data)
