# Importerer nødvendige moduler: time for tidsrelaterte funksjoner, board for tilgang til mikrokontrollerens pinne- og I2C-grensesnitt, adafruit_lps2x for tilgang til LPS22-sensoren
import time
import board
import adafruit_lps2x

# Oppretter en I2C-buss for kommunikasjon med sensorer
i2c = board.I2C()

# Oppretter en instans av LPS22-sensoren ved å bruke I2C-bussen
lps = adafruit_lps2x.LPS22(i2c)

# Uendelig løkke for kontinuerlig lesing og utskrift av sensordata
while True:
    # Skriver ut trykket fra sensoren med to desimaler og enheten hektopascal
    print("Pressure: %.2f hPa" % lps.pressure)
    # Skriver ut temperaturen fra sensoren med to desimaler og enheten Celsius
    print("Temperature: %.2f C" % lps.temperature)
    # Venter i ett sekund før neste avlesning for å unngå å overbelaste sensoren eller mikrokontrolleren
    time.sleep(1)
