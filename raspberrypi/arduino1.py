#Revison 1.0 (2014-04-22)
#move common function to another file
#
import sys
basepath='/home/pi/project'
sys.path.append(basepath)
import mycommon

import os.path
import datetime

dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
logfileprefix='arduino'
logfilename='/var/log/iot/'+logfileprefix+'.log'

jsonfile = basepath+'/iot-test-142f0511ddc8.json'
if (os.path.exists(jsonfile) == False):
       jsonfile = 'iot-test-142f0511ddc8.json'

scope = ['https://spreadsheets.google.com/feeds']
sheetname='IoT'
sheet=1

serialport='/dev/ttyUSB0'
sensordata=mycommon.get_raw_serialdata(serialport)

sensordata=mycommon.get_serial2sensor(sensordata)
print str(sensordata)
mycommon.log_to_file('Starting ...',logfilename)

mycommon.update_sheet(jsonfile,scope,sheetname,sheet,sensordata)

mycommon.log_to_file(str(sensordata),logfilename)
mycommon.log_to_file('finished.',logfilename)



