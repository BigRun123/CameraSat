import string, random, time
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

s2py = Scratch2Py("KahootPodium")
cloudproject = s2py.scratchConnect(965522461)
print(cloudproject.readCloudVar("Sensors"))
while True:
    try:
        cloudproject.setCloudVar("Sensors", encode_string(str(random.randint(0,10000000))))
        time.sleep(0.1)
        
    except:
        print("Error")
        cloudproject = s2py.scratchConnect(965522461)
    
print(decode_string(cloudproject.readCloudVar("Sensors")))
