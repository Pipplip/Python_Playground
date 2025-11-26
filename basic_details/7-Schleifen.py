"""
Schleifen

bei einer Break Bedingung kann man ein else nach der Schleife verwenden
while x:
    break
else:
    y

"""

""" 
 while 
"""
i = 1
while i <= 4:
    print(i, i**2)
    i += 1
# 1 1
# 2 4
# 3 9
# 4 16

# break, continue
liste = eval(input("Liste mit positiven Zahlen eingeben"))
n = len(liste)
i = 0
previous = None
erg = []
while i < n:
    current = liste[i]
    i += 1
    if current == previous:
        continue
    if current <= 0:
        print("Ncht positive Zahl gefunden")
        break
    erg.append(current)
    previous = current
    
print(erg)
# Eingabe [37,99,17,17,17,-3]
# Ausgabe [37,99,17]

"""
for gibt es nicht, nur foreach
"""
languages = ["deutsch","englisch","französich"]
for language in languages:
    print(language)
    
forTest = ["ham","egg","nuts"]
for food in forTest:
    if food == "ham":
        print("No more ham please")
        break
    print("Great "+food)
else:
    print("I'm glad, no ham!")
