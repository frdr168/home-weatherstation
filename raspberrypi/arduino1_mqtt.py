#Revison 1.0 (2016-07-14)
#
import sys
basepath='/home/pi/project'
sys.path.append(basepath)
import mycommon

import os.path
import datetime

from Adafruit_IO import Client
aio = Client('9b7d3ba55b8244018a291d0206d0a50a')

serialport='/dev/ttyUSB0'
sensordata=mycommon.get_raw_serialdata(serialport)

sensordata=mycommon.get_serial2sensor(sensordata)
print str(sensordata)
if (len(sensordata[0])==3): 
    print sensordata[0][1]
    aio.send('MQ135',float(sensordata[0][1]))

#mycommon.update_sheet(jsonfile,scope,sheetname,sheet,sensordata)


