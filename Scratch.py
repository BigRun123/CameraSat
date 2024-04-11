import string, time
from scratch2py import Scratch2Py 

def encode_string(string):
    encoded_string = ""

    for char in string:
        if characters.find(char) < 10:
            encoded_string += "0" + str(characters.find(char))

        else:
            encoded_string += str(characters.find(char))

    return encoded_string

def decode_string(string):
    decoded_string = ""

    for bit in [string[i:i+2] for i in range(0, len(string), 2)]:
        decoded_string += characters[int(bit)]

    return decoded_string

characters = string.printable[:95]
initialized = False

while not initialized:
	initialized = True

	try:
		s2py = Scratch2Py("KahootPodium", "Stsha001")

	except:
		print("Init error")
		initialized = False
		time.sleep(2)

print("Init succsess")
time.sleep(5)

cloudproject = s2py.scratchConnect(965522461)

f = open("Log.txt", "r")
l = open("Links.txt", "r")

counter = 0

while True:
	complete = False

	while not complete:
		complete = True

		try:
			line1 = f.readlines()[-2][:-2]
			f.seek(0)

		except:
			complete = False

	complete = False

	while not complete:
		complete = True

		try:
			line2 = l.readlines()[-1][:-1]
			l.seek(0)

		except:
			complete = False

	data = encode_string(line1 + ";" + line2)

	data1 = data[:256]
	data2 = data[256:]

	try:
		cloudproject.setCloudVar("Sensor 1", data1)
		cloudproject.setCloudVar("Sensor 2", data2)

	except:
		print("Cloud error")


	if counter >= 50:
		try:
			s2py = Scratch2Py("KahootPodium","Stsha001")
			cloudproject = s2py.scratchConnect(965522461)
			counter = 0
		except:
			continue

	counter += 1
	time.sleep(0.5)
