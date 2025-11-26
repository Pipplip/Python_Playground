"""
Dictionary

entspricht einer Map in Java
also key - value (Mapping)

keine feste Reihenfolge im Dictionary

als Schlüssel dürfen nur unveränderliche Datentypen verwendet werden, also z.B. keine Listen.
Tupel aber geht, weil diese unveränderbar sind
"""

map1 = {}
map2 = {"key1" : "value1", "key2" : "value2", "key3" : "value3"}
print(map2["key1"]) # "value1"
map2["key3"] = "value3a"
map2.get("key1") # value1


# Verschachtelung
de_en = {"rot":"red", "blau":"blue"}
en_de = {"red":"rot", "blue":"blau"}
de_fr = {"rot":"rouge", "blau":"bleu"}
print("French word for 'red' is: " + de_fr[en_de["red"]])

dictionaries = {"en_de":en_de, "de_fr":de_fr}
print(dictionaries["de_fr"]["blau"]) # bleu

# Fehler Vermeidung
"red" in en_de # True
"brown" in en_de # False

color = input("Farbe?")
if color in en_de:
    print("vorhanden!")
else:
    print("nicht vorhanden")
    
"""
 Methoden
"""
# clear()
dictionaries.clear()

# copy()
d = en_de.copy()
# ACHTUNG: Bei verschachtelten Dictionaries deepcopy verwenden

# dict.fromkeys()
food = {"ham", "eggs", "spam"}
d = dict.fromkeys(food, "enjoy")
print(d) # {'eggs':'enjoy', 'ham':'enjoy', 'spam':'enjoy'}

# items() (liefert Mengenähnliches Objekt)
items = en_de.items() # items = en_de (also alle key.value)

# keys()
keys = en_de.keys() # liefert eine Liste an keys

# pop() - Löschen eines keys
pop = en_de.pop("red")

# popitem() - Löschen eines beliebigen key-value Paares
# Aufruf ohne Parameter
en_de.popitem()

# setdefault() - fügt ein neues key-value hinzu, falls noch nicht vorhanden
# Wenn schon vorhanden, passiert nichts
en_de.setdefault("brown","braun") # wird in die Dic. hinzugefügt
en_de.setdefault("red","pink") # wird nicht hinzugefügt, weil es red schon gibt

# update() - fügt key-value hinzu und überschreibt vorhandene
en_de2 = {"yellow":"gelb", "pink":"pink"}
en_de.update(en_de2) # en_de wird erweitert und oder überschrieben

"""
Operatoren
"""
# Anzahl
len(en_de)

# zip-Funktion - Matrix erstellen
z1 = [11, 12, 13]
z2 = [21, 22, 23]
z3 = [31, 32, 33]
T = zip(z1, z2, z3)
print(list(T)) # [(11,21,31), (12,22,32), (13,23,33)]

# Dictionaries aus Listen erstellen
gerichte = ["Pizza", "Sauerkraut", "Hamburger"]
laender = ["Italien", "Deutschland", "USA"]
#print(list(zip(laender, gerichte)))

landesueblich = dict(zip(laender, gerichte))
print(landesueblich["Deutschland"])












