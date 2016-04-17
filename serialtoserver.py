import serial
import json

url = "asdfasdf"
count = 0
light = 0
temp = 0
sound = 0
json = ''
location = "bcc"
with serial.Serial('/dev/ttyS0', 9600, timeout=2) as ser:
	line = ser.readline()
	if count%3 == 0:
		light = int(line)
	elif count%3 == 1:
		temp = int(line)
	else:
		sound = int(line)
	count = (count + 1 )% 3
	if not count:
		json = json.dumps({"light": light, "temperature": temp, "sound": sound, "location", location})
