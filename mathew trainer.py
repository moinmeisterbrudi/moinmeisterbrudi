#Wir importieren das modul random
import random
import time
print("hallo weist du wie alt du bist")     



print("Moin zu dir zum mathe trainer . viel glück")    
    
nochmal = "ja"
punkte = 0          
max_punkte = 0      
     
while nochmal == "ja" or nochmal == "Ja":
          
  rechenzeichen = random.choice(["+","-","*","/"])          
  
  if rechenzeichen == "+":          
      zahl1 = random.randint(0, 100)     
      zahl2 = random.randint(0, 1000-zahl1)   
  if rechenzeichen == "-":              
      zahl1 = random.randint(0, 1000)
      zahl2 = random.randint(0, zahl1)
  if rechenzeichen == "*":     
      zahl1 = random.randint(0, 100)    
      zahl2 = random.randint (0, int(1000 / zahl1))                            
  if rechenzeichen == "/":   
      zahl1 = random.randint(0, 1000)   
      zahl2 = random.randint(1,int(1000 / zahl1))
  
  
  startzeit = time.time()
     
  endzeit = time.time()  


  if rechenzeichen == "*":
      max_punkte = max_punkte + 1 
      if zahl1 * zahl2 == antwort:
          print("Richtig!")      zahl1 = zahl1 * zahl2
      else:
          print("Froooong!Die richtigr Antwort wäre" (zahl1 + zahl2) + "gewesen.")              
   
  antwort = int(input("Was ist " + str(zahl1) + rechenzeichen + str(zahl2) + "? "))
                       
                                                                                                                                                                                      
  if rechenzeichen == "+":                                                                                           
      max_punkte = max_punkte + 1  
      if zahl1 + zahl2 == antwort:
        print("Richtig!")     
        punkte = punkte + 1                         
      else:     
          print("Froooong!Die richtigr Antwort wäre" (zahl1 + zahl2) + "gewesen.")

  if rechenzeichen == "-":                              
      max_punkte = max_punkte + 1 
      if zahl1 - zahl2 == antwort:
        print("Richtig!")
        punkte = punkte + 1
        
      else:
          print("Froooong!Die richtigr Antwort wäre" (zahl1 + zahl2) + "gewesen.")

  if rechenzeichen == "/":
      max_punkte = max_punkte + 1 
      if zahl1 / zahl2 == antwort:
        print("Richtig!")
        punkte = punkte + 2
      else:
        print("Froooong!Die richtigr Antwort wäre" (zahl1 + zahl2) + "gewesen.")
      
  nochmal = input("Nochmal spielen? ")
    
  print("Du hast " + str(punkte) + " Punkte von " + str(max_punkte) + " Punkte bekommen! 



 
  