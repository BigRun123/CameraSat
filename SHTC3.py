# Importerer nødvendige moduler: time for tidsrelaterte funksjoner, board for tilgang til mikrokontrollerens pinne- og I2C-grensesnitt, adafruit_shtc3 for tilgang til SHTC3-sensoren
import time
import board
import adafruit_shtc3

# Oppretter en I2C-buss for kommunikasjon med sensorer
i2c = board.I2C()

# Oppretter en instans av SHTC3-sensoren ved hjelp av I2C-bussen
sht = adafruit_shtc3.SHTC3(i2c)

# Uendelig løkke for kontinuerlig lesing og utskrift av sensordata
while True:
    # Leser temperaturen og relativ fuktighet fra sensoren
    temperature, relative_humidity = sht.measurements
    # Skriver ut temperaturen med to desimaler og enheten Celsius
    print("Temperature: %0.2f C" % temperature)
    # Skriver ut relativ fuktighet med to desimaler og enheten prosent (%)
    print("Humidity: %0.2f %%" % relative_humidity)
    # Skriver ut en tom linje for å skille mellom hver runde av sensordatautskrift
    print("")
    # Venter i ett sekund før neste avlesning for å unngå å overbelaste sensoren eller mikrokontrolleren
    time.sleep(1)
