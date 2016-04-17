import serial
import json

url = "asdfasdf"
count = 0
light = 0
temp = 0
sound = 0
json = ''
location = "bcc"
with serial.Serial('/dev/ttyACM0', 9600, timeout=2) as ser:
	while True:
		try:
			line = ser.readline()
			if line[0] == 'l':
				light = int(line[2:-4])
			elif line[0] == 't':
				temp = int(line[2:-4])
			elif line[0] == 's':
				sound = int(line[2:-4])
			count = (count + 1 )% 3
			if not count:
				json = json.dumps({"light":light,"temperature":temp,"sound":sound,"location":location})
				print(json)
		except:
			print("not working")s
			continue
