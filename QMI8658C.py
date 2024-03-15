# Importerer nødvendige moduler: time for tidsrelaterte funksjoner, board for tilgang til mikrokontrollerens pinne- og I2C-grensesnitt, qmi8658c for tilgang til QMI8658C-sensoren
import time
import board
import qmi8658c

# Oppretter en I2C-buss for kommunikasjon med sensorer
i2c = board.I2C()

# Oppretter en instans av QMI8658C-sensoren ved hjelp av I2C-bussen
mpu = qmi8658c.QMI8658C(i2c)

# Uendelig løkke for kontinuerlig lesing og utskrift av sensordata
while True:
    # Leser akselerasjonsdata fra sensoren
    ac = mpu.acceleration
    # Leser gyroskopdata fra sensoren
    gy = mpu.gyro
    # Skriver ut akselerasjonsdata med to desimaler og enheten m/s^2 for hver aksenhet
    print(f"Acceleration: X:{ac[0]:.2f}, Y:{ac[1]:.2f}, Z:{ac[2]:.2f} m/s^2")
    # Skriver ut gyroskopdata med to desimaler og enheten rad/s for hver aksenhet
    print(f"Gyro X:{gy[0]:.2f}, Y:{gy[1]:.2f}, Z:{gy[2]:.2f} rad/s")
    # Skriver ut temperaturen med to desimaler og enheten Celsius
    print(f"Temperature: {mpu.temperature:.2f} C")
    # Skriver ut en tom linje for å skille mellom hver runde av sensordatautskrift
    print("")
    # Venter i ett sekund før neste avlesning for å unngå å overbelaste sensoren eller mikrokontrolleren
    time.sleep(1)
