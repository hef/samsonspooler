import makerbot_driver
import serial
from makerbot_driver.FileReader.constants import hostFormats
from makerbot_driver.FileReader.constants import slaveFormats
import struct


class ReplicatorDriver:
        
    def connect(self, port='/dev/ttyACM0'):
        self.r = makerbot_driver.s3g()
        file = serial.Serial(serial_port, 115200, timeout=1)
        self.r.writer = makerbot_driver.Writer.StreamWriter(file)

    def print_file(self, file):

        reader = makerbot_driver.FileReader.FileReader()
        reader.file = open(file)
        payloads = reader.ReadFile()

        self.r.capture_to_file("samson.s3g")
        for paylaod in payloads:
            command = self.payload_to_command(payload) 
            self.r.writer.send_command(command)
        response = r.end_capture_to_file()
        self.r.playback_capture("samson.s3g")

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

