# Begrüßung
print("Herzlich willkommen zu Tic Tac Toe!")

# Liste für die Positionen anlegen und initialisieren
spielfeld = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

runde = 1
while runde <= 5:

    # Spielfeld ausgeben
    reihe1 = spielfeld[0] + " | " + spielfeld[1] + " | " + spielfeld[2]
    reihe2 = spielfeld[3] + " | " + spielfeld[4] + " | " + spielfeld[5]
    reihe3 = spielfeld[6] + " | " + spielfeld[7] + " | " + spielfeld[8]
    trennreihe = "---------"
    print(reihe1)
    print(trennreihe)
    print(reihe2)
    print(trennreihe)
    print(reihe3)

    # Spieler 1 nach seinem Zug fragen
    pos = input("Spieler 1, auf welches Feld möchtest du setzen? ")

    # Zug durchführen
    if spielfeld[int(pos) - 1] == pos:
        spielfeld[int(pos) - 1] = "x"

    # Prüfen, ob Spieler 1 gewonnen hat
    if spielfeld[0] == "x" and spielfeld[1] == "x" and spielfeld[2] == "x":
        print("Glückwunsch Spieler 1, du hast gewonnen!")
        break
    if spielfeld[3] == "x" and spielfeld[4] == "x" and spielfeld[5] == "x":
        print("Glückwunsch Spieler 1, du hast gewonnen!")
        break
    if spielfeld[6] == "x" and spielfeld[7] == "x" and spielfeld[8] == "x":
        print("Glückwunsch Spieler 1, du hast gewonnen!")
        break
    if spielfeld[0] == "x" and spielfeld[3] == "x" and spielfeld[6] == "x":
        print("Glückwunsch Spieler 1, du hast gewonnen!")
        break
    if spielfeld[1] == "x" and spielfeld[4] == "x" and spielfeld[7] == "x":
        print("Glückwunsch Spieler 1, du hast gewonnen!")
        break
    if spielfeld[2] == "x" and spielfeld[5] == "x" and spielfeld[8] == "x":
        print("Glückwunsch Spieler 1, du hast gewonnen!")
        break
    if spielfeld[0] == "x" and spielfeld[4] == "x" and spielfeld[8] == "x":
        print("Glückwunsch Spieler 1, du hast gewonnen!")
        break
    if spielfeld[2] == "x" and spielfeld[4] == "x" and spielfeld[6] == "x":
        print("Glückwunsch Spieler 1, du hast gewonnen!")
        break

    # Spielfeld ausgeben
    reihe1 = spielfeld[0] + " | " + spielfeld[1] + " | " + spielfeld[2]
    reihe2 = spielfeld[3] + " | " + spielfeld[4] + " | " + spielfeld[5]
    reihe3 = spielfeld[6] + " | " + spielfeld[7] + " | " + spielfeld[8]
    trennreihe = "---------"
    print(reihe1)
    print(trennreihe)
    print(reihe2)
    print(trennreihe)
    print(reihe3)

    # Spieler 2 nach seinem Zug fragen
    pos = input("Spieler 2, Auf welches Feld möchtest du setzen? ")
    
    # Zug durchführen
    if spielfeld[int(pos) - 1] == pos:
        spielfeld[int(pos) - 1] = "o"

    # Prüfen, ob Spieler 1 gewonnen hat
    if spielfeld[0] == "o" and spielfeld[1] == "o" and spielfeld[2] == "o":
        print("Glückwunsch Spieler 2, du hast gewonnen!")
        break
    if spielfeld[3] == "o" and spielfeld[4] == "o" and spielfeld[5] == "o":
        print("Glückwunsch Spieler 2, du hast gewonnen!")
        break
    if spielfeld[6] == "o" and spielfeld[7] == "o" and spielfeld[8] == "o":
        print("Glückwunsch Spieler 2, du hast gewonnen!")
        break
    if spielfeld[0] == "o" and spielfeld[3] == "o" and spielfeld[6] == "o":
        print("Glückwunsch Spieler 2, du hast gewonnen!")
        break
    if spielfeld[1] == "o" and spielfeld[4] == "o" and spielfeld[7] == "o":
        print("Glückwunsch Spieler 2, du hast gewonnen!")
        break
    if spielfeld[2] == "o" and spielfeld[5] == "o" and spielfeld[8] == "o":
        print("Glückwunsch Spieler 2, du hast gewonnen!")
        break
    if spielfeld[0] == "o" and spielfeld[4] == "o" and spielfeld[8] == "o":
        print("Glückwunsch Spieler 2, du hast gewonnen!")
        break
    if spielfeld[2] == "o" and spielfeld[4] == "o" and spielfeld[6] == "o":
        print("Glückwunsch Spieler 2, du hast gewonnen!")
        break

    runde = runde + 1