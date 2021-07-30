"""
Datentypen und Variablen

Variablen referenzieren in Python Objekte (Speicherplätze)
Variable kann unterschiedliche Datentypen haben und sind nicht statisch deklariert
wie das z.B. in C oder Java ist (also z.B: int a oder String s)

"""

# Erzeugung eines Integer-Objekts und welches wir mit i referenzieren.
# Definiton
i = 42
print("Wert von i: ", i)

# Identitätsfunktion
print(id(i)) # gibt Speicherbereich zurück z.B. 2969159822928

x = i / 3.0 + 5.8
print(x) # 19.8


i += 1
print(i) # 43

# Operatoren:
# (+) Summe a + b
# (-) Differenz a - b
# (*) Produkt a * b
# (/) Quotient a / b
# (//) ganzzahlige Division a // b (abgerundet)
# (%) Modulo a % b
# (abs) Betrag von a abs(a)
# (**) Potenzieren a^b

"""
Ganze Zahlen Integer
in Python unbegrenzt

"""
# Binär-Zahlen (führend 0b oder 0B)
b = 0b101010 # 42

# Oktalzahlen (0o oder 0O)
o = 0o10 # 8

# Hexadezimal (0x oder 0X)
h = 0x10 # 16

#
# Umwandlung int in String
#
hu = hex(19) # '0x13'
type(hu) # <class 'str'>
bu = bin(65) # '0b1000001'
ou = oct(65) # '0o101'

"""
Float Fliesskomma Zahlen
"""
f = 2.34
f2 = 3.14e2 # 3,14*10^2

"""
Strings
"""
# siehe 2-Strings-Listen-Tupel

"""
Boolean
"""
t = True
false = False

print(not t) # False
print(t and false) # False
print(t or false) # True
print(t and not false) # True


"""
Komplexe Zahlen
a+b*j (a und b sind reele Zahlen und j imaginär)
"""
kompleX = 3 + 4j
kompleY = 2 - 4.5j
print(kompleX + kompleY) # 5-0.5j
print(kompleX * kompleY) # 24-5.5j

"""
Typumwandlung
"""

# mit type() kann man den Typ ausgeben lassen
# isinstance geht auch
inst = 42.0
print(isinstance(inst,float)) # True
print(isinstance(inst,(float, int))) # True: float or int

typen = 42
print(type(typen)) # <class 'int'>
typen = "Hallo"
print(type(typen)) # <class 'str'>
typen = [3,9,17] 
print(type(typen)) # <class 'list'>

first_name = "Thomas"
last_name = "Müller"
age = 20
# explizite Typeumwandlung
print(first_name + " " + last_name + ": " + str(age)) # Thomas Müller: 20

"""
Globale und lokale Variablen
"""
# da s nicht übergeben wird oder lokal in der Funktion definiert wurde,
# bezieht sie ihren Wert aus der globalen Variable s
def f():
    print(s)
    
s = "Hallo Welt"
f() # Hallo Welt

# Bsp 2: was passiert wenn s in der Funktion verändert wird?
def f2():
    # print(s2) darf hier nicht stehen, würde Fehler werfen, 
    # da Variable nicht lokal und global in der Funktion sein kann
    #
    # global s2
    # print(s2) würde aber gehen
    s2 = "Hallo Funktion"
    print(s2)
s2 = "Hallo Welt"
f2()
print(s2)

# Ausgabe:
# Hallo Funktion
# Hallo Welt




 