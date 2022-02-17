print("Hallo!")

klasse = int(input ("In welche Klasse gehst du?"))

if klasse < 5:
    print("Grundschule")
else:
    print("Weiterführende Schule!")
    print ("Warum nicht?")
tier = int (input("Hast du ein Haustier"))

if tier > 0:
    tierart = input ("Was für eines!")
    if tierart == "Hund":
        print ("Ein treuer Begleiter!")
    if tierart == "Igel":
        print("Eine stachelige angelegenheit")
    if tierart == "Axolotle":
        print ("Eine komische angelegenheit")
    if tierart == "weißer Hei":
        print ("Eine tolle angelegenheit")
    if tierart == "Blizard":
        print ("kosmetische angelegenheit")
else:
    print("Warum nicht?")

import random

zahl1 = 12 
zahl2 = 33
antwort = int (input ("Was ist" + str (zahl1) + " + " + str (zahl2) + "? "))
zahl1 = random. randint(0,100)
zahl2 = random. randint(0,100)
if antwort == zahl1 + zahl2:
        print (" Du Genie!")
else:
        print ("nnnnnnnnööööööööö")