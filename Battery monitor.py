import smbus

addr = 0x10
bus = smbus.SMBus(1)
vcellH = bus.read_byte_data(addr,0x03)
vcellL = bus.read_byte_data(addr,0x04)
socH = bus.read_byte_data(addr,0x05)
socL = bus.read_byte_data(addr,0x06)

capacity = (((vcellH&0x0F)<<8)+vcellL)*1.25
electricity = ((socH<<8)+socL)*0.003906

print("Capacity = " + str(round(capacity)) + "mV")
print("Electricity percentage = " + str(round(electricity)) + "%")