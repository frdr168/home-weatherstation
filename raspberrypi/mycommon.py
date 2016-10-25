#Revision 1.1(2016-04-29)
#array data format to upload googlesheet
# Revision 1.0 (2016-04-22)
# common library
#
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import serial
import sys
import os.path
import datetime

def mydate():
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return dt

def begin_serial(serialport):
    ser = serial.Serial(
          port=serialport,
          baudrate = 9600,
          parity=serial.PARITY_NONE,
          stopbits=serial.STOPBITS_ONE,
          bytesize=serial.EIGHTBITS,
          timeout=1
         )
    return ser

def get_raw_serialdata(serialport):
    ser=begin_serial(serialport)
    rawdatas=[]
    cnt=0
    tmpdata=ser.readline().split("\r\n")
    print tmpdata
    while (tmpdata[0] == ''):
          tmpdata=ser.readline().split("\r\n")
          if (tmpdata[0] != ''):
              break
    print tmpdata
    if (tmpdata[0] == "Starting"):
        while True:
              tmpdata=ser.readline().split("\r\n")
              if (tmpdata[0] == "Stop"):
                  ser.close()
                  break
              tmp=tmpdata[0].split('|')
              rawdatas.append([])
              for i in tmp:
                  rawdatas[cnt].append(i)
              cnt=cnt+1
    return rawdatas

def get_serial2sensor(data):
    newdata=[]
    tmp=data
    newdata.append([])
    for j in tmp:
        newdata[0].append(j[3])
        newdata[0].append(j[4])
        newdata[0].append(j[5])
    return newdata

def log_to_file(msg,filename):
    if (os.path.exists(filename)):
        f = open(filename,'a')
        f.write(mydate() + ' ' + msg + '\r\n')
        f.close()

def authorize_sheet(jsonfile,scope):
    try:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonfile, scope)
        gc = gspread.authorize(credentials)
        print "credentials ok"
    except IOError:
        print 'google driver error'
    return gc
		
def update_sheet(jsonfile,scope,sheetname,sheet,sensordata):
    gc=authorize_sheet(jsonfile,scope)
    for sh in range(len(sheet)):
        wks = gc.open(sheetname).get_worksheet(sheet[sh])
        lastrow=len(wks.get_all_values())
        #print lastrow
        newrow = lastrow + 1
        #print len(sensordata)
        for j in sensordata[sh]:
            #print str(j)
            j.insert(0,mydate())
            j.insert(0,newrow)
            #print str(j)
            wks.insert_row(j,newrow)
            print str(j)
            newrow = newrow + 1


