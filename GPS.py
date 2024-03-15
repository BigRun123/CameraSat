
# Importerer serial-modulen for seriell kommunikasjon og pynmea2-modulen for å analysere NMEA-data
import serial
import pynmea2

# Åpner en seriell forbindelse på den angitte porten ("/dev/ttyS0")
ser = serial.Serial("/dev/ttyS0")

# Uendelig løkke for å kontinuerlig motta og prosessere GPS-data
while True:
    # Leser en linje med data fra den serielle forbindelsen og dekoder den fra bytes til UTF-8-tegnsettet
    gps_data = ser.readline().decode("UTF-8")
    
    # Sjekker om den mottatte NMEA-meldingen er av typen GNGGA
    if gps_data[0:6] == "$GNGGA":
        # Parser NMEA-meldingen med pynmea2 for å trekke ut relevant informasjon
        msg = pynmea2.parse(gps_data)
        
        # Henter kvalitetsindikatoren for GPS-signalet
        qual = msg.gps_qual
        
        # Henter breddegraden, lengdegraden, høyden og antall synlige satellitter fra NMEA-meldingen
        lat = msg.latitude
        lon = msg.longitude
        alt = msg.altitude
        sat = msg.num_sats
        
        # Sjekker om GPS-signalet er av god kvalitet (kvalitetsindikator lik 1)
        if qual == 1:
            # Skriver ut informasjonen om breddegrad, lengdegrad, høyde og antall synlige satellitter
            print("Latitude =", round(lat, 6), "Longitude =", round(lon, 6), "Altitude =", round(alt, 6), "Satellites:", int(sat))
        else:
            # Hvis GPS-signalet er av dårlig kvalitet, skrives en melding om at det ikke er signal
            print("No Signal!")
```

Disse kommentarene forklarer hva hver linje med kode gjør og hvordan den fungerer.
