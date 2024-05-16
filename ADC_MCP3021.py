import smbus2
import time

class MCP3021:

	bus = smbus2.SMBus(1)	# rpi revision 2
	
	def __init__(self, address = 0x4b):
		self.address = address
		
	def readRaw(self):
		# read word (16 bits) as int
		rd = self.bus.read_word_data(self.address, 0)
		# exchange high and low bytes
		data = ((rd & 0xFF) << 8) | ((rd & 0xFF00) >> 8)
		# ignore two least significant bits
		return data >> 2
		
adc = MCP3021()


while True:
	raw = adc.readRaw()
	print("Raw data: ", raw)
	time.sleep(1)
