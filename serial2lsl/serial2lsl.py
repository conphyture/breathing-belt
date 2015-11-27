# Caution, quick'n dirty!

import serial, time

port = '/dev/ttyACM0'
baudrate = 115200

ser = serial.Serial(port, baudrate)
time.sleep(1)

while True:
  line = ""
  try:
    line = ser.read(1)
  except:
    print "error"
  print line
  time.sleep(0.002)
  
ser.close()
