"""
Eine anonyme Funktion oder Lambda-Funktion ist eine Funktion,
die nicht über einen Namen verfügt. Eine solche Funktion kann deshalb nur über Verweise angesprochen werden.
Der lambda-Operator bietet eine Möglichkeit, anonyme Funktionen, also Funktionen ohne Namen, zu schreiben und zu benutzen. 
Lambda-Funktionen kommen aus der funktionalen Programmierung. 
Sie können eine beliebige Anzahl von Parametern haben, führen einen Ausdruck aus und liefern den Wert
dieses Ausdrucks als Rückgabewert zurück.

-> bessere Alternative zu lambdas sind Listen-Abstractionen (list comprehension)
-> Definiert Mengen in Python

"""
# Bsp: Funktion mit Argument x, die die Summe von x und 42 zurückgibt
#lambda x: x + 42

y = (lambda x: x + 42)(3)
print(y) #45

# Bsp 2:
f42 = lambda x: x + 42
print(f42(3)) # 45

# Bsp 3:
def anwenden(f, liste):
    ergebnis = []
    for element in liste:
        ergebnis.append(f(element))

    return ergebnis

print(anwenden(f42, range(10))) # [42, 43, 44, 45, 46, 47, 48, 49, 50, 51]


"""
List comprehension
"""
print([(x,y) for x in range(1,7) for y in range(1,7) if x + y == 7])
# [(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)]

# anstatt
t = []
for x in range(1,7):
    for y in range(1,7):
        if x + y == 7:
            t.append( (x,y) )
print(t)

# Bsp 2: x|10 <= x <= 100∧ x teilbar durch 4}
print([ x for x in range(10,101) if not x % 4])
# [12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100]

"""
Mengen Abstraktion
"""
# analog zu list comprehension, nur das eine Menge zurückgeliefert wird
print({ x for x in range(10,101) if not x % 4})
# {12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100}