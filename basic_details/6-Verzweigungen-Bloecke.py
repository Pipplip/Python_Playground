"""
Verzweigungen

Doppelpunkt leitet Einrückung ein
Leerzeichen oder Tab. Geht beides
ABER: Nicht beides mischen

"""

alter = int(input("Dein Alter: "))

if alter < 12:
    print("Du bist jünger als 12.")
else:
    print("Du bist älter als 12")
    
    
# Verschachtelte Anweisung
if alter < 12:
    print("Du bist jünger als 12.")
elif alter < 16:
    print("Du bist zwischen 12 und 16")
else:
    print("Älter als 16")
    
# Operatoren
# == -> 42 == 42 True, [1,2]==[1,2] True
# != -> 42 != 43 True, {1,2] != 17 True
# < / > -> 4 < 12 True, "Ti" < "Tisc" True
# <= / >= -> 4 <= 4 True
# and, or, not -> Verbinden von Verknüpfungen

a = 1
b = 100
c = 33
if c > a and c < b:
    print("Passt")

# Alles was nicht False ist, ist True
liste = []
if liste:
    print("Liste enthält Elemente")
else:
    print("Keine Elemente")