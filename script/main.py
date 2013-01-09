#!/usr/bin/env python
import makerbot_driver
import serial
from pprint import pprint

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

#do things
#warning, this chunk of code is wrong!
#for payload in payloads:
#	filtered_payload = []
#	for element in payload:
#		if type(element) == type("string"):
#			for char in element:
#				filtered_payload.append(char)
#		else:
#			filtered_payload.append(element)
#	pprint(filtered_payload)
#	r.writer.send_command(filtered_payload)

r.set_toolhead_temperature(0,0)
r.toggle_axes(['x','y','z','a','b'],False)

