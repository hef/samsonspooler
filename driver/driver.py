import makerbot_driver
import serial
from makerbot_driver.FileReader.constants import hostFormats
from makerbot_driver.FileReader.constants import slaveFormats
import struct
from pprint import pprint
from time import sleep


class ReplicatorDriver:
        
    def connect(self, serial_port='/dev/ttyACM0'):
        self.r = makerbot_driver.s3g()
        try:
            file = serial.Serial(serial_port, 115200, timeout=1)
            self.r.writer = makerbot_driver.Writer.StreamWriter(file)
        except serial.SerialException:
            #todo log that this happened
            file = open("samson.s3g",'wb')
            self.r.writer = makerbot_driver.Writer.FileWriter(file) 

    def print_file(self, file):

        reader = makerbot_driver.FileReader.FileReader()
        reader.file = file
        payloads = reader.ReadFile()

        try:
            self.r.capture_to_file("samson.s3g")
        except NotImplementedError:
            pass

        for payload in payloads:
            command = self.payload_to_command(payload) 
            pprint(command)
            self.r.writer.send_action_payload(command)
            sleep(1)
        try:
            response = self.r.end_capture_to_file()
        except NotImplementedError:
            pass

    def payload_to_command(self, payload):
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

