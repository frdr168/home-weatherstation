#Revision 1.0(2016-06-28)
#
import sys
basepath='/home/pi/project'
sys.path.append(basepath)
import mycommon
import mypisensor

import os.path
import datetime

from Adafruit_IO import Client
aio = Client('9b7d3ba55b8244018a291d0206d0a50a')

sensordata=[]
sensordata.append(mypisensor.get_raw_sensor('DHT11',4))
sensordata.append(mypisensor.get_raw_sensor('BMP085',0))

print str(sensordata)
#print len(sensordata)
#print len(sensordata[0])
#print len(sensordata[1])

#print len(sensordata[0][0])
#print len(sensordata[1][0])

aio.send('DHT11_temp',float(sensordata[0][0][0]))
aio.send('DHT11_humd',float(sensordata[0][0][1]))
aio.send('BMP085_temp',float(sensordata[1][0][0]))
aio.send('BMP085_pres',float(sensordata[1][0][1]))
aio.send('BMP085_alti',float(sensordata[1][0][2]))
aio.send('BMP085_pasa',float(sensordata[1][0][3]))

