#!/usr/bin/python
import urllib
import time

import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
pin = 4
api_key=xxxxxxxxxxxxxxxx

def log(temp,humid):
    with open("/home/pi/src/log/temperature.csv","a") as f:
        f.write("{},{},{}\n".format(time.time(),temp,humid))
 
while True:

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    temperature = temperature*9.0/5.0 + 32.0

    print('Posting: {} Temp: {} F Humid: {}'.format(time.strftime('%x %r'),temperature,humidity))
    log(temperature,humidity)
    field1 = temperature;
    field2 = humidity;
    post_data_str = 'https://api.thingspeak.com/update?api_key={}&field1={}&field2={}'.format(api_key,field1,field2)

    try:
        result = urllib.urlopen(post_data_str)
    except:
        print('ERROR Posting')

    time.sleep(15)

