#!/usr/bin/env python
import makerbot_driver
import serial
from pprint import pprint
from makerbot_driver.FileReader.constants import hostFormats
import struct

reader = makerbot_driver.FileReader.FileReader()
reader.file = open("20mm_Calibration_Box.s3g")
payloads = reader.ReadFile()

#setup
#r = makerbot_driver.s3g()
#file = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
#r.writer = makerbot_driver.Writer.StreamWriter(file)

# home all the things
#r.find_axes_maximums(['x', 'y'], 500, 60)
#r.find_axes_minimums(['z'], 500, 60)
#r.recall_home_positions(['x', 'y', 'z', 'a', 'b'])

#do things
for payload in payloads:
    command_code = payload[0]
    fmt = "<" + "".join(hostFormats[command_code])
    args =  payload[1:]
    print "{0} {1} {2}".format(command_code, fmt, args)
    command = struct.pack(fmt,*args)
    pprint(command)


#r.set_toolhead_temperature(0,0)
#r.toggle_axes(['x','y','z','a','b'],False)

