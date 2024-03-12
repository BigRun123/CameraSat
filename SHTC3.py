import time
import board
import adafruit_shtc3

i2c = board.I2C()
sht = adafruit_shtc3.SHTC3(i2c)

while True:
    temperature, relative_humidity = sht.measurements
    print("Temperature: %0.2f C" % temperature)
    print("Humidity: %0.2f %%" % relative_humidity)
    print("")
    time.sleep(1)