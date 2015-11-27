# Caution, quick'n dirty!

import serial, time
from pylsl import StreamInfo, StreamOutlet

# parameters for com port
# TODO: from command line
port = '/dev/ttyACM0'
baudrate = 115200
# 2ms pause in arduino firmware: 500Hz
samplingrate = 500
# rate for spamming stdout
displaySamplingRate = 10

ser = serial.Serial(port, baudrate)

# create LSL StreamOutlet
info = StreamInfo('breath','breath',1,samplingrate,'float32','conphyturebreathing1337')
outlet = StreamOutlet(info)

# some time for init?
#time.sleep(0.5)

n=0
while True:
  line = ser.readline()
  value = 0
  # convert string to float (remove trailing line break at the same time...)
  try:
    value = float(line)
  except:
    # silently discard conversion problem
    pass
  #TODO: won't work if rates not dividers
  if n%(samplingrate/displaySamplingRate) == 0:
    print value
  outlet.push_sample([value])
  n+=1
  #time.sleep(0.002)
  
ser.close()
