"""
Sequentielle Datentypen

Strings, Listen und Tupel sind Sequenzen in Python
Vorteil: gleiche Aufrufe für alle Sequenzen

Listen = veränderbar also z.B. liste[0] = 1
Tupel = unveränderbar, z.B. tupel[0] = 1 -> Exception

Listen und Tupel können gleich ausgelesen werden. Nur beim Schreiben und Verändern unterscheiden sie sich.

"""

print(dir(str)) # alle Methoden für Strings
# print(help(str)) # alle Methoden für Strings

"""
 Strings
"""
s1 = 'Mit einfachen Anführungszeichen'
s2 = "mit doppelten"
s3 = '''"Mit dreifachen"'''
s4 = "Ich bin mehrzeilig \
und man trennt mich mit einem Backlash"
s5 = "Zeilenumbruch \n"

# für Dokus
s6 = """Erste Zeile
Zweite Zeile
Dritte Zeile \
und nochmal Dritte Zeile"""

print(s6)

#Escape Zeichen
# \\ Backlash
# \' Hochkomma
# \" Anführungszeichen
# \b Backspace
# \f Seitenumbruch
# \n Zeilenumbruch
# \NNAME Unicode-Zeichen Bsp: \NGREEK SMALL LETTER PI
# \t horizontaler Tab
# \uXXXX 16-Bit Unicode
# \uXXXXXXXX 32-Bit Unicode
# \v vertikaler Tabulator
# \ooo ASCII Zeichen oktal
# \xhh ASCII Zeichen hexadezimal

# Aussetzen von Escape Zeichen mit R
s7 = R"\nMacht keinen Zeilenumbruch"

# Indizierung
s8 = "Hallo"
print(s8[0]) # H
print(s8[-1]) # o

#-5 -4 -3 -2 -1
# H  a  l  l  o
# 0  1  2  3  4


# Substring: Slicing
s9 = "Hello World"
s9a = s9[1:5] # 'ello'
s9b = s9[:5] # 'Hello'
s9c = s9[1:] # 'ello World'

# Slicing mit Schrittweise
# txt[Anfang,Ende,Schrittweise]
s10 = [3,8,12,4,9,14,23,7,21,37]
print(s10[::3]) # [3,4,23,37]

s11 = [3,6,9,12,7]
print(s11[3:1:-1]) # [12,9]

# Länge bestimmen
s12 = "To be or not to be"
print(len(s12)) # 18

s13 = ["Berlin", "Hamburg"]
print(len(s13)) # 2




"""
Listen
Leerzeichen dürfen zwischen Inhalten stehen
mit Komma getrennt und in [] Klammern geschrieben
"""
l1 = [3,99,"Ein Text"]
l2 = [ 42, 65, [45, 89], 88 ]
print(l2[0]) # 42
print(l2[2]) # [45,89]
print(l2[2][1]) # 89

# Listen kopieren
l3 = ["a","b","c","d"]
l4 = l3[:]
l4[1] = "x"
print(l3) # ['a', 'b', 'c', 'd']
print(l4) # ['a', 'x', 'c', 'd']

# ACHTUNG: Bei verschachtelter Liste (auch Dictionaries) geht das nicht mit [:]
# Bei verschachtelten Listen deepcopy verwenden
from copy import deepcopy
l5 = ["a","b",["ac","ad"]]
l6 = deepcopy(l5)
l6[2][1] = "d"
l6[0] = "c"
print(l6) # ['c', 'b', ['ac', 'd']]


"""
Tupel werden mit () Klammern geschrieben
"""
t1 = (3,99,"Ein Text")
t2 = ( 42, 65, [45, 89], 88 )