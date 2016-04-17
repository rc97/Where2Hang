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
	if line[1] == 'l'
		light = int(line[2:])
	elif line[1] == 't'
		temp = int(line[2:])
	elif line[1] == 's':
		sound = int(line[2:])
	count = (count + 1 )% 3
	if not count:
		json = json.dumps({"light": light, "temperature": temp, "sound": sound, "location", location})
