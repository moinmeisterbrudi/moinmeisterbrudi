# Wir importieren das Modul random
import random
import time

print("Herzlich willkommen zum Mathetrainer, viel Erfolg!")

nochmal = "ja"
punkte = 0
max_punkte = 0

while nochmal == "ja" or nochmal == "Ja":

    # Rechenaufgabe erstellen
    rechenzeichen = random.choice(["+", "-", "*", "/"])

    if rechenzeichen == "+":
        zahl1 = random.randint(0, 1000)
        zahl2 = random.randint(0, 1000 - zahl1)
    if rechenzeichen == "-":
        zahl1 = random.randint(0, 1000)
        zahl2 = random.randint(0, zahl1)
    if rechenzeichen == "*":
        zahl1 = random.randint(0, 1000)
        zahl2 = random.randint(0, int(1000 / zahl1))
    if rechenzeichen == "/":
        zahl1 = random.randint(0, 1000)
        zahl2 = random.randint(1, int(1000 / zahl1))
        zahl1 = zahl1 * zahl2

    startzeit = time.time()

   
    antwort = int(input("Was ist " + str(zahl1) + rechenzeichen + str(zahl2) + "? "))

    endzeit = time.time()

    # Auswertung
    if rechenzeichen == "+":
        max_punkte = max_punkte + 1
        if zahl1 + zahl2 == antwort:
            print("Richtig! Du hast " + str(endzeit - startzeit) + "Sekunden gebraucht.")
            punkte = punkte + 1
        else:
            print("Richtig! Du hast " + str(endzeit - startzeit) + "Sekunden gebraucht.")

    if rechenzeichen == "-":
        max_punkte = max_punkte + 1
        if zahl1 - zahl2 == antwort:
            print("Richtig! Du hast " + str(endzeit - startzeit) + "Sekunden gebraucht.")
            punkte = punkte + 1
        else:
            print("Richtig! Du hast + str(endzeit - startzeit) + "Sekunden gebraucht.")

    if rechenzeichen == "*":
        max_punkte = max_punkte + 2
        if zahl1 * zahl2 == antwort:
            print("Richtig! Du hast + str(endzeit - startzeit) + "Sekunden gebraucht.")
            punkte = punkte + 2
        else:
            print("Richtig! Du hast + str(endzeit - startzeit) + "Sekunden gebraucht.")
    
    if rechenzeichen == "/":
        max_punkte = max_punkte + 2
        if zahl1 / zahl2 == antwort:
            print("Richtig! Du hast + str(endzeit - startzeit) + "Sekunden gebraucht.")
            punkte = punkte + 2
        else:
            print("Richtig! Du hast + str(endzeit - startzeit) + "Sekunden gebraucht.")

    nochmal = input("Möchtest du nocheinmal spielen? ")

print("Du hast " + str(punkte) + " Punkte von " + str(max_punkte) + " Punkten erreicht")
