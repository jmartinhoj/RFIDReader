#!/usr/bin/python3

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import requests
import json
import time
import requests

url = "http://192.168.8.16/people/authorize"

reader = SimpleMFRC522()
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
try:    
    GPIO.setwarnings(False)
    url = "http://192.168.8.18:3000/people/authorize"
    while(True):
        id = reader.read_id()
        payload = "{\n\t\"RFID\": \"" + str(id) + "\"\n}"
        headers = {
                'content-type': "application/json",
                'cache-control': "no-cache",
                }
        response = requests.request("POST", url, data=payload, headers=headers)
        y = json.loads(response.text)
        print(y["authorized"])
        if(y["authorized"] == True):
            GPIO.output(7, GPIO.HIGH)
            GPIO.output(16,GPIO.HIGH)
            time.sleep(3)
            GPIO.output(16, GPIO.LOW)
            GPIO.output(7, GPIO.LOW)
        else:
            GPIO.output(12,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(12, GPIO.LOW)


finally:
    GPIO.cleanup()


