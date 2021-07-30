"""
Formatierte Ausgabe und Strings formatieren

format Methode der Stringklasse priorisieren

Default print Methode:
print(value1, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
sep gibt an, wie die Ausgabe zwischen values aussieht

"""
print("a","b","c",sep=".") # a.b.c

print("a","b",end=" :-)") # a b :-) - kein return beim Ende der Ausgabe, sondern ein Smiley

file = open("formatierteAusgabe.txt","w")
print("a","b", file=file)
file.close()

# Fehler-Kanal
import sys
print("Fehler", file=sys.stderr)

# mit String Modulo Operator %
# %[flags][width][.precision]type
# Bsp: &6.2f
# 6 = totale Anzahl an Zeichen (inkl. Dezimalpunkt, Nachkommastellen etc.)
# . = Einleitung Dezimalteil
# 2 = Anzahl Dezimalteil (Nachkommastellen)
# f = Platzhalter (hier: float)

"""
Übersicht wichtigste Platzhalter:
d = Integer, Dezimal
i = Integer, Dezimal
o = Oktalzahl
u = Dezimalzahl
x oder X = hexadezimalzahl
e oder E = Fließkommazahl exponentiell
c = ein Zeichen
s = Zeichenkette
"""

# format-Methode
form1 = "Erstes {0}, Zweites {1}".format(47,11)
print(form1) # Erstes 47, Zweites 11

form2 = "Erstes Arg: {0:5d}, Preis: {1:8.2f}".format(453, 59.058)
print(form2) # Erstes Arg:   453, Preis:   59.06

form3 = "{0:6.2f} - {0:6.3f}".format(1.4148)
print(form3) #  1.41 -  1.415

form4 = "{a:5d} - {p:8.2f}".format(a=453, p=59.058)
print(form4) #  453 -    59.06

# rechtsbündige Ausgabe mit > / linksbündig mit <
form5 = "{0:>20s}: {1:6.2f}".format("Hallo Welt", 7.99)
print(form5)

"""
weitere Sting Methoden
"""
# center
str1 = "Python"
str1.center(10)
print(str1) # '  Python  '
str1.center(10,"+")
print(str1) # '++Python++'

# ljust (linksbünig) / rjust (rechtsbündig)
str2 = "Training"
str2.ljust(12)
print(str2) # 'Training    '

# zfill (mit Nullen auffüllen)
str3 = "123456"
str3.zfill(10)
print(str3) # '0000123456'


