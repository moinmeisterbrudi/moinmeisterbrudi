def ausgabe():
    reihe1 = spielfeld[0] + " | " + spielfeld[1] + " | " + spielfeld[2]
    reihe2 = spielfeld[3] + " | " + spielfeld[4] + " | " + spielfeld[5]
    reihe3 = spielfeld[6] + " | " + spielfeld[7] + " | " + spielfeld[8]
    trennreihe = "_________"
    print(reihe1)
    print(trennreihe)
    print(reihe2)
    print(trennreihe)
    print(reihe3)

def prüfung(spielfeld, spieler):
    if spieler == 1:
        symbol = "x"
    else:
        symbol = "o"
    # Prüfen, ob der spieler1 gewonnen hat
    if spielfeld[0] == symbol and spielfeld[1] == symbol and spielfeld[2] == symbol:
        print ("Glückwunsch Spieler2, du hast gewonnen!")
    if spielfeld[3] == symbol and spielfeld[4] == symbol and spielfeld[5] == symbol:
        print ("Glückwunsch Spieler2, du hast gewonnen!")
    if spielfeld[6] == symbol and spielfeld [7] == symbol and spielfeld[8] ==symbol:
        print ("Glückwunsch Spieler2, du hast gewonnen!")
    if spielfeld[0] == symbol and spielfeld[3] == symbol and spielfeld[6] == symbol:
        print ("Glückwunsch Spieler2, du hast gewonnen!")
    if spielfeld[1] == symbol and spielfeld[4] == symbol and spielfeld[7] == symbol:
        print ("Glückwunsch Spieler2, du hast gewonnen!")
    if spielfeld[2] == symbol and spielfeld[5] == symbol and spielfeld[8] == symbol:
        print ("Glückwunsch Spieler2, du hast gewonnen!")
    if spielfeld[0] == symbol and spielfeld[5] == symbol and spielfeld[8] == symbol:
        print ("Glückwunsch Spieler2, du hast gewonnen!d")
    if spielfeld[0] == symbol and spielfeld[1] == symbol and spielfeld[2] == symbol:
        print ("Glückwunsch Spieler2, du hast gewonnen!")
    if spielfeld[2] == symbol and spielfeld[4] == symbol and spielfeld[6] == symbol:
        print ("Glückwunsch Spieler2, du hast gewonnen!")

print("Herzlich Wilkommen zu Tic Tac Toe!")

# Liste für die Positionen anlegen und installieren
spielfeld = ["1", "2", "3", "4" , "5", "6" , "7" , "8" , "9"]

spieler = 1
runde = 1

while runde <= 9:
     
    ausgabe()

    # Spieler 1 nach seinem Zug fragen0,
    pos = input ("Spieler" +  str(spieler) + ", auf welches Feld möchtest du setzen? ")

    # Zug durchführen 
    if spielfeld[int(pos) - 1] == pos:
        if spieler == 1:
            spielfeld[int(pos) - 1]  = "x"
        else:
            spielfeld[int(pos) - 1]  = "o"
    
    prüfung(spielfeld,spieler)

    if spieler == 1:
        spieler = 2
    else:
        spieler = 1
    runde = runde + 1
     

     