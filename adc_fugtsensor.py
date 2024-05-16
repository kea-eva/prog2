8umikimport smbus2
import time

# find adressen till i2cpython 
# sudo i2cdetect -y 1

bus = smbus2.SMBus(1)		# rpi revision 2
i2c_address = 0x4b		# address

while True:

	# read words ( 2 bytes) as int - 0 is comm byte
	rd = bus.read_word_data(i2c_address, 0)
	# exchange high and low bytes
	data = ((rd & 0xFF) << 8) | ((rd & 0xFF00) >> 8)
	# ignores the  two least significant bits
	data = data >> 2
	print("Data: ", data)
	time.sleep(1)
