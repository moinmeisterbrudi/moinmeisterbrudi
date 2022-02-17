print("Hi , hast ne Aufgabe?")

gültig = False
while gültig == False: 
    try:

        zahl1 = int(input("Welche Zahl nimmst erst ?"))
        gültig = True
    except:
       print("Es sin Zahlen als Eingabe erlaubt")



while gültig == False:
    rechenzeichen = input("Nimmst du +, -, * oder /?  ")
    if rechenzeichen == "+" or rechenzeichen == "-" or rechenzeichen == "*" or rechenzeichen == "/":
        gültig = True
    else:
        print("Es ist nur +, -, *  und / erlaubt")




zahl2 = int(input("Welche Zahl nimmst du als nächstes ?"))

if rechenzeichen == "+":
    print("Das Ergebnis lautet" + zahl1 + zahl2 )
elif rechenzeichen == "-":
    print("Das Ergebnis lautet" +  str(zahl1 - zahl2 ))
elif rechenzeichen == "*":
    print("Das Ergebnis lautet" + str(zahl1 * zahl2))
else :
    print("Das Ergebnis lautet " + str(zahl1 / zahl2 ))





    gültig = False
while gültig == False: 
    try:

        zahl2 = int(input("Welche Zahl nimmst erst ?"))
        gültig = True
    except:
       print("Es sin Zahlen als Eingabe erlaubt")



while gültig == False:
    rechenzeichen = input("Nimmst du +, -, * oder /?  ")
    if rechenzeichen == "+" or rechenzeichen == "-" or rechenzeichen == "*" or rechenzeichen == "/":
        gültig = True
    else:
        print("Es ist nur +, -, *  und / erlaubt")