# Importerer nødvendige moduler: string for å manipulere strenger, random for å generere tilfeldige tall, time for tidsrelaterte funksjoner
import string
import random
import time
# Importerer Scratch2Py-biblioteket for å kommunisere med Scratch-prosjekter
from scratch2py import Scratch2Py

# Funksjon for å kode en streng ved å konvertere hvert tegn til en tallverdi
def encode_string(string):
    encoded_string = ""

    for char in string:
        # Sjekker om tegnet er en spesiell karakter, hvis ja, legg til en ledende null
        if characters.find(char) < 10:
            encoded_string += "0" + str(characters.find(char))
        else:
            encoded_string += str(characters.find(char))
            
    return encoded_string
        
# Funksjon for å dekode en kodet streng tilbake til den opprinnelige strengen
def decode_string(string):
    decoded_string = ""
    
    # Deler den kodede strengen opp i tosifrede biter og konverterer dem tilbake til tegn
    for bit in [string[i:i+2] for i in range(0, len(string), 2)]:
        decoded_string += characters[int(bit)]
    
    return decoded_string

# Definerer tegnsettet som består av utskriftbare tegn fra ASCII-tabellen
characters = string.printable[:95]

# Oppretter en Scratch2Py-instans for å kommunisere med et Scratch-prosjekt med navnet "KahootPodium", og passord ***************
s2py = Scratch2Py("KahootPodium","***************")

# Kobler til det angitte Scratch-prosjektet via skyen og får tilgang til skyvariabelen "Sensors"
cloudproject = s2py.scratchConnect(965522461)
print(cloudproject.readCloudVar("Sensors"))

# Uendelig løkke for å generere tilfeldige tall, kode dem og sende dem til skyen
while True:
    try:
        # Genererer et tilfeldig tall mellom 0 og 10 millioner, koder det og sender det til skyvariabelen "Sensors"
        cloudproject.setCloudVar("Sensors", encode_string(str(random.randint(0,10000000))))
        # Venter i 0.1 sekund før neste iterasjon
        time.sleep(0.1)
        
    # Håndterer unntak (feil)
    except:
        # Skriver ut feilmelding
        print("Error")
        # Kobler til Scratch-prosjektet på nytt hvis det oppstår en feil
        cloudproject = s2py.scratchConnect(965522461)
    
# Printer den dekodede strengen fra skyvariabelen "Sensors"
print(decode_string(cloudproject.readCloudVar("Sensors")))
