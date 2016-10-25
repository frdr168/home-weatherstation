#Revision 1.1(2014-04-29)
#Add BMP085
#Revison 1.0 (2014-04-26)
# pi digit pin data
#
import sys
basepath='/home/pi/project'
sys.path.append(basepath)
import mycommon
import mypisensor

import os.path
import datetime

dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
logfileprefix='pisensor'
logfilename='/var/log/iot/'+logfileprefix+'.log'

jsonfile = basepath+'/iot-test-142f0511ddc8.json'
if (os.path.exists(jsonfile) == False):
       jsonfile = 'iot-test-142f0511ddc8.json'

scope = ['https://spreadsheets.google.com/feeds']
sheetname='IoT'
sheet=[]
sheet.append(0)
sheet.append(2)

sensordata=[]
sensordata.append(mypisensor.get_raw_sensor('DHT11',4))
sensordata.append(mypisensor.get_raw_sensor('BMP085',0))

print str(sensordata)
#print str(sensordata_bmp)
mycommon.log_to_file('Starting ...',logfilename)

mycommon.update_sheet(jsonfile,scope,sheetname,sheet,sensordata)

mycommon.log_to_file(str(sensordata),logfilename)

#mycommon.update_sheet(jsonfile,scope,sheetname,sheet_bmp,sensordata_bmp)

#Emycommon.log_to_file(str(sensordata_bmp),logfilename)

mycommon.log_to_file('finished.',logfilename)

