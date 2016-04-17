import serial

count = 0
with serial.Serial('/dev/ttyS0', 9600, timeout=2) as ser:
	line = ser.readline()
	count%3 something
	count+=1
