import time
import board
import adafruit_lps2x

i2c = board.I2C()
lps = adafruit_lps2x.LPS22(i2c)

while True:
    print("Pressure: %.2f hPa" % lps.pressure)
    print("Temperature: %.2f C" % lps.temperature)
    time.sleep(1)