"""
Stapelspeicher (stack) für Listen

Vorstellbar wie ein Bücherstapel
Auf Stapel legen (push/append), nehmen (pop) und schauen was ganz oben liegt (peek)

In Python:
    append() oder '+': am Ende des Stapels hinzufügen - append bevorzugen, da performanter
    insert(): an beliebige Stelle des Stapels hinzufügen
    remove(): entfernen eines Elements
    pop(): letzte Element nehmen und ausschneiden
    pop(i): Element i nehmen und ausschneiden
    extend(t): an eine Liste mehrere Elemente anhängen
    index(): Gibt die Stelle des Elements im Stack zurück

"""
import time
print(time.time())

stack = ["eins", "zwei"]
stack.append("drei")
pop = stack.pop()
print(pop) # 'drei'
print(stack) # ['eins', 'zwei']

# extend
stack1 = [1,2,3,4]
stack1.extend([5,6,7,8])
print(stack1) # [1, 2, 3, 4, 5, 6, 7, 8]

# remove
stack2 = ["red","green","blue","yellow"]
if(stack2.count("green") > 0):
    stack2.remove("green")
print(stack2) # ['red', 'blue', 'yellow']

# index
stack3 = ["red","green","blue","yellow"]
print(stack3.index("green")) # 1

# insert
stack3.insert(1, "pink")
print(stack3) # ['red', 'pink', 'green', 'blue', 'yellow']

# Sternoperator
first, *remainder = 35, 99, 27, 18
print(first) # 35
print(remainder) # [99, 27, 18]

name = "Max Mai Mustermann"
firstname, middlename, surname = name.split()
print(firstname) # Max
print(middlename) # Mai
print(surname) # Mustermann

"""
 Sortierung
"""
stack4 = [6,8,7,3,8,4]
stack4.sort() # liefert kein Ergebnis, sondern sortiert nur das Objekt, deshalb hier kein print
print(stack4) # [3, 4, 6, 7, 8, 8]

stack5 = [6,8,7,3,8,4]
print(sorted(stack5)) # [3, 4, 6, 7, 8, 8]

# Umkehrung der Sortierung
stack6 = [6,8,7,3,8,4]
print(sorted(stack6, reverse=True)) # [8, 8, 7, 6, 4, 3]
# stack6.sort(reverse=True)

# Eigene Sortierung



