#Revision 1.1 (2014-04-29)
#Add BMP085
#Revison 1.0 (2014-04-26)
#move common function for pi sensor 
#

import RPi.GPIO as GPIO
import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085
import sys

def begin_sensor(s):
    if (s == "DHT11"):
           sensor=Adafruit_DHT.DHT11
    if (s == "BMP085"):
           sensor=BMP085.BMP085()
    return sensor

def get_raw_sensor(s,DPIN):
    d=[]
    d.append([])
    sensor=begin_sensor(s)
    if (s == "DHT11"):
          humidity, temperature = Adafruit_DHT.read_retry(sensor,DPIN)
          d[0].append(str(temperature))
          d[0].append(str(humidity))
          return d
    if (s == "BMP085"):
           d[0].append('{0:0.2f}'.format(sensor.read_temperature()))
           d[0].append('{0:0.2f}'.format(sensor.read_pressure()))
           d[0].append('{0:0.2f}'.format(sensor.read_altitude()))
           d[0].append('{0:0.2f}'.format(sensor.read_sealevel_pressure()))
           return d

