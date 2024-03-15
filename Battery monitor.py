# Importerer smbus-modulen som tillater kommunikasjon med I2C-enheter
import smbus

# Definerer adressen til den I2C-enheten vi vil kommunisere med
addr = 0x10

# Oppretter en ny instans av SMBus med bussnummer 1
bus = smbus.SMBus(1)

# Leser ett byte med data fra adressen 0x03 på enheten med adressen addr (spenning høy byte)
vcellH = bus.read_byte_data(addr, 0x03)

# Leser ett byte med data fra adressen 0x04 på enheten med adressen addr (spenning lav byte)
vcellL = bus.read_byte_data(addr, 0x04)

# Leser ett byte med data fra adressen 0x05 på enheten med adressen addr (elektrisitetsprosent høy byte)
socH = bus.read_byte_data(addr, 0x05)

# Leser ett byte med data fra adressen 0x06 på enheten med adressen addr (elektrisitetsprosent lav byte)
socL = bus.read_byte_data(addr, 0x06)

# Beregner kapasitet basert på spenningen, og justerer for skalering
capacity = (((vcellH & 0x0F) << 8) + vcellL) * 1.25

# Beregner elektrisitetsprosent basert på verdiene for høy og lav byte, og justerer for skalering
electricity = ((socH << 8) + socL) * 0.003906

# Skriver ut kapasitet i millivolt
print("Capacity = " + str(round(capacity)) + "mV")

# Skriver ut elektrisitetsprosenten
print("Electricity percentage = " + str(round(electricity)) + "%")
