import time, board, math, adafruit_lps2x, adafruit_shtc3, stts22h, qmi8658c, smbus, IMU

imu = IMU.IMU()
i2c = board.I2C()
lps = adafruit_lps2x.LPS22(i2c)
mpu = qmi8658c.QMI8658C(i2c)
sht = adafruit_shtc3.SHTC3(i2c)
stts = stts22h.STTS22H(i2c)
bus = smbus.SMBus(1)
i2c = board.I2C()

f = open(f"Log.txt","a")
f.truncate(0)


counter = 0
start_time = time.time()

start_press = lps.pressure
time.sleep(5)

start_press = lps.pressure

while True:

	try:
		socH = bus.read_byte_data(0x10, 0x05)
		socL = bus.read_byte_data(0x10, 0x06)
		electricity = round((((socH << 8) + socL) * 0.003906), 2)
	except:
		electricity = None

	try:
		tempSht, humSht = sht.measurements
	except:
		tempSht, humSht = None, None

	try:
		tempLps = lps.temperature
	except:
		tempLps = None

	try:
		tempSttsh = stts.temperature
	except:
		tempSttsh = None

	try:
		pressLps = round(lps.pressure, 4)
		#altLps = 8500 * math.log(start_press/lps.prssure)
		altLps = round(44330 * (1-(lps.pressure/start_press)**(1/5.255)), 2)
	except:
		pressLps = None
		altLps = None

	try:
		Gyro, Accel = imu.QMI8658_Gyro_Accel_Read()
	except:
		Gyro, Accel = None, None

	try:
		Mag = imu.AK09918_MagRead()
	except:
		Mag = None

	try:
		tempMpu = imu.QMI8658_readTemp()
	except:
		tempMpu = None

	
	try: 
		ax = Accel[0]
		ay = Accel[1]
		az = Accel[2]

		gx = Gyro[0]
		gy = Gyro[1]
		gz = Gyro[2]

		mx = Mag[0]
		my = Mag[1]
		mz = Mag[2]
	
		aA = round(math.sqrt(ax**2 + ay**2 + az**2), 4)
		gA = round(math.sqrt(gx**2 + gy**2 + gz**2), 4)
		mA = round(math.sqrt(gx**2 + gy**2 + gz**2), 4)

	except:
		ax = None
		ay = None
		az = None

		gx = None
		gy = None
		gz = None

		mx = None
		my = None
		mz = None

		aA = None
		gA = None
		mA = None

	current_time = round(1000*(time.time()-start_time))

	f.write(f"CameraSat;{counter};{current_time};{electricity};{altLps};{pressLps};{tempSttsh};{tempLps};{tempMpu};{humSht};{ax};{ay};{az};{aA};{gx};{gy};{gz};{gA};{mx};{my};{mz};{mA}\n")


	counter += 1

	f.flush()
