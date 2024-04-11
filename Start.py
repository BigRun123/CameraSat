import os

f = open("/boot/Autostart.txt", "r")

statement = f.readlines()[0]

if "True" in statement:
	os.system("python3 Starter.py")

