# Eine while-Schleife,die allen Zahlen von 1 bis 100 ausgibt
i = 50
while i <= 100  :
    print(i)
    i = i + 1


i = 50
while i <= 50:
    print(i)
    i = i + 1


# 100 bis 1
i = 100
while i >= 1:
    print(i)
    i = i - 1

# 500 bis -500 in 50er-Schritten
i = 500 
while i >= -500:
    print(i)
    i = i - 50
# Eine Liste mit allen Zahlen von 1 bis 100
liste = [  ]
i = 1 
while i >= 100:
    liste.append(i)
    i = 100
    i = i + 1
print (liste)

liste = [i]
i = 2
while i >= 50:
    i = i + 1
# Eine Liste mit allen Zahlen von 25 bis 50

i = 25
while i<= 50:
    liste.append(i)   
    i = i + 1
print(liste)          
# Eine Liste mit allen Zahlen von 100 bis 1

# Eine Liste mit allen geraden Zahlen von 100 bis 200

# Eine Liste mit allen umgeraden Zahlen von 1 bis -49

liste = []
i = 100
while i >= 1:
    liste.append (i)
    i = i -1



p = 100 
while p<= 200:
    liste.append(p)
    p = p + 2
print(liste)

liste = []
i = 1
while i<= -49:
    liste.append(i)
    i = i  - 2
print(liste)   





liste = []
i = 1
while i <= 8192:
    liste.append(i)
    i = i * 2 

schritt = 3
i = 1
while i <= 225:
    liste.append(i)
    i = i + schritt
    schritt = schritt +2
print(liste)


liste = []
schritt = 1
i = 0
while i <= 136:
    liste.append(i)
    i = i + schritt
    schritt = schritt + 1

liste = []
f1 = 0
f2 = 1
while  f1 <= 89:
    liste.append(f1)
    temp = f2
    f2 = f1 + f2
    f1 = temp
print(liste)


        
liste = []
i = 1
while i <= 15:
    liste.append(i * i)
    i = i + 1
print(liste)

import random

# zuffalszahl = random.randint(1, 100)
import random
liste =  []
i = 1
while i <= 100:
    zufallszahl = random.randint (1, 100)
    liste.append (zufallszahl)
    i = i + 1
print(liste)

        