"""
Mengen - Set

Ein Element kann in einem Set nicht doppelt vorkommen
veränderliche Objekte wie z.B. Listen sind als Sets nicht erlaubt
"""

set1 = {'Hamburg','Müchnen','Frankfurt'}
print('Berlin' in set1) #  False

set2 = set(('Paris', 'Paris', 'Lyon'))
print(set2) # {'Paris','Lyon'}

set3 = set("Hallo")
print(set3) # {'H','a','l','o'}
print(type(set3)) # <class 'set'>

# frozensets
set4 = frozenset(["Miami"])
#set4.add("Florida") # wirft Fehler, weil man nicht hinzufügen darf bei frozensets

"""
Operatoren
"""
# add() - Elemente hinzufügen
set5 = set1.copy()
set5.add('Stuttgart')
print(set5)

# clear()
set6 = set5.copy()
set6.clear()

# copy()
set7 = {'Aalen'}
set7a = set7.copy()
set7.clear()
print(set7a) # {'Aalen'}

# ACHTUNG Zuweisung
set8 = {'Heidenheim'}
set8a = set8
set8.clear()
print(set8a) # set()

# difference - Differenz zwischen zwei Mengen
set9 = {"a","b","c","d"}
set10 = {"a","e"}
set11 = set9.difference(set10)
print(set11) # set(["b","c","d"])
# statt difference() kann man auch '-' benutzen
# set11 = set9 - set10

# difference_update() - entfernt alle Elemente einer Menge aus einer Menge x=x-y
set12 = {"a","b","c","d"}
set13 = {"b","c"}
set12 = set12.difference_update(set13)
print("set12: ")
print(set12) # {'a','d'}

# discard() - entfernen eines Elements (wenn nicht vorhanden passiert nichts)
set14 = {"a","b","c","d"}
set14.discard("a")
print(set14) # "b","c","d"

# remove() - wie dicard, nur das ein Fehler geworfen wird, wenn Element nicht vorhanden

# intersection() - Liefert Schnittmenge (gleiche Elemente zweier Sets)
set15 = {"a","b","c","d"}
set16 = {"a","g","d"}
print(set15.intersection(set16)) # 'd','a'

# isdisjoint() - True, wenn zwei Mengen eine leere Schnittmenge haben
set17 = {"a","b"}
set18 = {"c","d"}
print(set17.isdisjoint(set18)) # True

# issubset() - liefert True, wenn eine Untermenge vorhanden ist
set19 = {"a","b","c","d"}
set20 = {"c","d"}
print(set19.issubset(set20)) # False set19 < set20
print(set20.issubset(set19)) # True  set20 < set19 // set20 ist eine echte Untermenge von set19

# issuperset() - True, wenn x eine Obermenge von y ist
# x > y x enthält mindestens ein Element von y
set21 = {"a","b","c","d"}
set22 = {"c","d"}
print(set21.issuperset(set22)) # True

# pop() - liefert ein beliebiges Element der Menge und wird aus dieser entfernt
set23 = {"a","b","c","d"}
set24 = set23.pop()
print(set24) # z.B. 'b'
print(set23) # {'a', 'c', 'd'}





