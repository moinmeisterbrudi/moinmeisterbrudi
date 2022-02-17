import random

farben = ["rot", "blau", "grün" , "pink" , "gelb"]

farbe1 = random.choice(farben)
farben.remove(farbe1)
farbe2 = random.choice(farben)
farben.remove(farbe2)
farbe3 = random.choice(farben)


i = 1
while i <= 8:
   
    eingabe = input ("Versuch " + str(i) +  ":what u setzing  ? ")
    eingabe_liste = eingabe.split()
        
    schwarz, weiß = 0, 0
    if eingabe_liste[0] == farbe1:
        schwarz = schwarz + 1
    if eingabe_liste[1] == farbe2:
        schwarz = schwarz + 1
    if eingabe_liste[2] == farbe3:
        schwarz = schwarz + 1
    if eingabe_liste[0] == farbe2 or eingabe_liste[0] == farbe3:
        schwarz = schwarz + 1 
    if eingabe_liste[1] == farbe1 or eingabe_liste[1] == farbe3:   
        schwarz = schwarz + 1 
    if eingabe_liste[2] == farbe1 or eingabe_liste[2] == farbe2:     
        schwarz = schwarz + 1 
        
    
    print("Schwarz", schwarz, "Weiß:", weiß)

    if schwarz == 3:
        print("wallah richtig du bist begabt!")
        break

    if i == 8:  
        print("BBBBuuuuuuh du bist ultra schlecht hier ist die lösung: " + farbe1 + " " + farbe2 + " " + farbe3)
    i = i + 1   
