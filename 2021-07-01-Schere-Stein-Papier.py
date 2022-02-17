import random

#### : Wir begrüßen den Spieler freundlich
print("\nHerzlich willkommen zu Schere Stein Papier!")

### Variablen zum mitzählen der Punkte des Spielers und des Computers
punktestand_spieler = 0
punktestand_computer = 0
### Wie oft möchte der Spieler spielen?
runden = input ("Wie oft möchtest du spielen? ")

for i in range(int(runden)):
    ###Wir geben den Punktestand aus
    print("Punkte Spieler : " + str(punktestand_spieler) + " --- Punkte Computer: " + str(punktestand_computer))

    ### Wir fragen den Spieler, was er wählen möchte
    spielerwahl = input ("\nWas möchtest du wählen? ")

    ### Wir lassen den Computer zufällig wählen
    computerwahl = random.choice(["Schere","Stein","Papier"])
    print ("Der computer wählt" + computerwahl)

    if spielerwahl == "Schere" and computerwahl =="Schere":
        print ("Unentschieden!")
    if spielerwahl == spielerwahl == "Stein"  and computerwahl  =="Papier":
        print (" Computer gewinnt!")
        punktestand_computer = punktestand_computer + 1 
    if spielerwahl == "Stein"  and computerwahl =="Stein":
        print ("Unentschieden!")
    if spielerwahl == "Stein"  and computerwahl =="Schere":
        print ("Spieler gewinnt!")
        punktestand_spieler = punktestand_spieler +1
    if spielerwahl == "Schere" and computerwahl =="Papier":
        print ("Spieler gewinnt!")
        punktestand_spieler = punktestand_spieler + 1
    if spielerwahl == "Schere" and computerwahl =="Stein" :
        print ("Computer gewinnt! ")
        punktestand_computer = punktestand_computer +1
    if spielerwahl == "Papier" and computerwahl =="Papier":
        print ("Unentschieden!")
    if spielerwahl == "Papier" and computerwahl =="Schere":
        print ("Computer gewinnt!")
        punktestand_computer = punktestand_computer + 1
    if spielerwahl == "Papier" and computerwahl =="Stein":
        print ("Spieler gewinnt!")
        punktestand_spieler = punktestand_spieler + 1

### Endstand ausgeben und sagen, wer gewonnen hat
if punktestand_spieler > punktestand_computer:
    print ("Spieler hat gewonnen , herzlichen Glückwunsch!")
if punktestand_computer > punktestand_spieler:
    print ("Computer hat gewonnen!")
if punktestand_computer == punktestand_spieler:
    print ("Unentschieden!")
    