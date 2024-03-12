import serial
import pynmea2

ser = serial.Serial ("/dev/ttyS0")

while True:
    gps_data = ser.readline().decode("UTF-8")
    
    if gps_data[0:6] == "$GNGGA":
        msg = pynmea2.parse(gps_data)
        
        qual = msg.gps_qual
        lat = msg.latitude
        lon = msg.longitude
        alt = msg.altitude
        sat = msg.num_sats
        
        if qual == 1:
            print("Latitude =", round(lat, 6), "Longitude =", round(lon, 6), "Altitude =", round(alt, 6), "Satellites:", int(sat))
        
        else:
            print("No Signal!")