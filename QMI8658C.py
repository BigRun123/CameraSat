import time
import board
import qmi8658c

i2c = board.I2C()
mpu = qmi8658c.QMI8658C(i2c)

while True:
    ac = mpu.acceleration
    gy = mpu.gyro
    print(f"Acceleration: X:{ac[0]:.2f}, Y:{ac[1]:.2f}, Z:{ac[2]:.2f} m/s^2")
    print(f"Gyro X:{gy[0]:.2f}, Y:{gy[1]:.2f}, Z:{gy[2]:.2f} rad/s")
    print(f"Temperature: {mpu.temperature:.2f} C")
    print("")
    time.sleep(1)