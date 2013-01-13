#!/usr/bin/env python
import makerbot_driver
import serial
from pprint import pprint
from makerbot_driver.FileReader.constants import hostFormats
from makerbot_driver.FileReader.constants import slaveFormats
import struct

reader = makerbot_driver.FileReader.FileReader()
reader.file = open("20mm_Calibration_Box.s3g")
payloads = reader.ReadFile()

#setup
r = makerbot_driver.s3g()
file = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
r.writer = makerbot_driver.Writer.StreamWriter(file)

# home all the things
r.find_axes_maximums(['x', 'y'], 500, 60)
r.find_axes_minimums(['z'], 500, 60)
r.recall_home_positions(['x', 'y', 'z', 'a', 'b'])

def payload_to_command(payload):
    command_code = payload[0]
    fmt = "<B" + "".join(hostFormats[command_code])
    if command_code == 136:
        """ Tool Action Command """
        slave_command = payload[2]
        fmt = fmt + "".join(slaveFormats[slave_command])
        command = struct.pack(fmt,*payload)
    elif command_code == 149:
        command = struct.pack("<BBBBB",*payload[:-1])
        command += payload[-1]
        command += '\0'
        """ Display message """
        pass
    elif command_code == 153:
        """ Build start notification """
        command = struct.pack("<BI",*payload[:-1])
        command += payload[-1]
        command += '\0' 
    else:
        command = struct.pack(fmt,*payload)
    return command


r.capture_to_file("samson.s3g")
for paylaod in payloads:
    command = payload_to_command(payload) 
    r.writer.send_command(command)
response = r.end_capture_to_file()
print response
r.playback_capture("samson.s3g")

r.set_toolhead_temperature(0,0)
r.toggle_axes(['x','y','z','a','b'],False)

