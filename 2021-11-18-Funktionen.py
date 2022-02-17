from _typeshed import IdentityFunction


def positiv(zahl):
    if zahl < 0:
        print("positiv")
    else:
        print("Nicht positiv!")
positiv(5)

def größer(zahl1,zahl2):
    if zahl2 < zahl1:
        print(zahl1)
    else:
        print(zahl2)
größer(100, 200)

def doppeln(zahl):

    print(zahl * 2)
doppeln(123)

def summe(zahl1,zahl2):
    print(zahl1 + zahl2)
summe(5, 5)

def product(zahl1, zahl2, zahl3):
    print(zahl1 * zahl2 * zahl3)


def quadrat(zahl):
    print(zahl * zahl)
quadrat(4)

def länge(wort):
    print(len(wort)) 
länge("Straßenkreuzung")

def längeres(wort1, wort2):
    print(wort1, wort2 )

def längenunterschied(wort1, wort2):
    if (wort1) > len(wort2)):
        print(len(wort1) - len(wort2)
    else:
        print(len(wort1) - len(wort2))
        längenunterschied("Elefant" , "Haiflosse")


def erster(wort):
    print(wort[0])
erster("Onkel")

def gleich(wort1, wort2):
    if wort1[0] == wort2[0]:
        print("gleich")
    else
        print("ungleich")

def gleich_an_index(wort1, wort2, index)
    if wort1[index] == wort2[index]:
        print("Gleich")
    else:
        print("Ungleich")


def mit_a(wort):
    if wort[0] == "A":
        print("Ja")
    else:
        print("nein")


def zweiter_buchstabe(wort):
   print(wort[1])

def letzter_buchstabe(wort):
    print(wort[len(wort)])- 1])
letzter_buchstabe("Eisenbahn")

def buchstabe_an_stelle(wort, index)
    print(wort[index])
buchstabe_an_stelle("Wiese", 3)

def vorletzter_buchstabe(wort):
    print(wort[len))-2])  
vorletzter_buchstabe("Eisenbahn")

def erster_und_letzter(wort):
    print(wort[0] + wort[len(wort) - 1])
    

def erste_drei(wort):
    print(wort[0] + woort[1] + wort[2])



def länger_als_5(wort):
    if len (wort) > 5:
        print("Ja")
    else:
        print("Nein")

def gleich_lang(wort1, wort2):
    if len (wort1) == len(wort2):
        print("Ja")
    else:
        print("Nein")

def fast_gleich_lang(wort1, wort2):
    if len(wort1) == len(wort2):
        print("Ja")
    elif len(wort1) == len(wort2) + 1:
        print("Ja")

        print("Ja")
    elif len(wort1) == len(wort2) -1:
        print("Nein")

def doppeltes(zahl):
    return zahl * 2
d = doppeltes(10)
print(d)
dd = doppeltes(doppeltes(10))
print (dd)

def achtfaches_mit_rechenzeichen(zahl):
    return zahl * 8 

def achtfaches_ohne_rechenzeichen(zahl):
    return doppeltes(doppeltes(doppeltes(zahl)))
print(achtfaches_ohne_rechenzeichen(4))

def a_durch_b(a, b):
    return a / b
print(a_durch_b(10, 5))

def größere(a, b)
   if a > b:
       return a
    else:
        return b
print(größere(123, 234))

def größte(a, b, c)
    if a > b and a > c:
        return a
    elif b >  a and b > c:
        return b 
    else:
        return c


def gleich(a, b):
    if a == b:
        return True
    else:
        return False
























































































































    dfff
