"""
Funktionen
---
def funktionsname(Parameterliste)
    Anweisung(en)
    
funktionsname(Argumente)
---

Call by Object Reference

Wenn man unveränderliche Argumente (z.B. Int, String, Tupel) an Funktion übergibt = Call by Value
Die Referenz des unver. Arguments wird an Funktion übertragen.
Die Funktion kann diese Argumente nicht verändern.

Auch veränderliche Argumente werden per Referenz an eine Funktion übertragen.
Allerdings können einzelne Elemente eines veränderlichen Arg. in der Funktion verändert werden

"""
def sayHello(name):
    return "Hello " + name
    
n = "World"
print(sayHello(n))

# optionale Parameter
def sayHello2(name="everybody"):
    return "Hello" + name
    
def addiereZahlen(a=2,b=3,c=4):
    return a + b + c

print(addiereZahlen()) # 2+3+4 = 9
print(addiereZahlen(5)) # 5+3+4 = 12
print(addiereZahlen(5,6)) # 5+6+4 = 15
print(addiereZahlen(c=10)) # 2+3+10 = 15


"""
DocString
"""
def test():
    """ function prints 'test' """
    print("test")

print("DocString der Funktion test: " + test.__doc__) # DocString der Funktion test:  function prints 'test'


"""
einfache Rückgabewerte
"""
def no_return(x,y):
    c = x+y

print(no_return(1,2)) # None

def return_sum(x,y):
    return x + y
print(return_sum(1,2)) # 3


"""
sowohl globale als auch lokale Variablen können in Funktionen verwendet werden
Wenn man globale Variablen in Funktionen verarbeiten will, muss man diese in der
Funktion angeben
"""

def f():
    global s
    print(s)
    s = "Perl"
    print(s)
s = "Python"
f()
print(s) # Python, Perl, Perl
# wenn es s vor dem Funktionsaufruf nicht global gab, gibt es sie nach global s in
# der Funktion nun global

"""
Beispiele Referenzen
Beispiel 1: unveränderliche Argumente
"""
def ref_demo1(x):
    print("x=",x," id=",id(x))
    x = 42
    print("x=",x," id=",id(x))

refValue1 = 2
ref_demo1(refValue1)
print(id(refValue1))
# x= 2  id= 1981937838416
# x= 42  id= 1981937839696
# 1559264717136

# refValue1 bleibt unverändert global erhalten!
# Erst wenn die übergebene Referenz in der Funktion verändert wird, wird ein neuer
# Speicherbereich angelegt
# Python verhält sich zuerst wie call by reference, d.h. man benutzt/referenziert 
# zunächst dasselbe Objekt
# Sobald x in der Funktion einen neuen Wert zugewiesen bekommt
# verhält es sich wie call by value (x erhält ein eigenes Objekt)

"""
Beispiel 2: veränderliche Argumente
"""
def ref_demo2(liste):
    print("Liste: ",liste, " id=", id(liste))
    liste += ["3","4"]
    print("Liste: ",liste, " id=", id(liste))
    
refList1 = ["1","2"]
print("Liste: ",refList1, " id=", id(refList1))
ref_demo2(refList1)
print("Liste: ",refList1, " id=", id(refList1))
    
# Liste:  ['1', '2']  id= 1314353803840
# Liste:  ['1', '2']  id= 1314353803840
# Liste:  ['1', '2', '3', '4']  id= 1314353803840
# Liste:  ['1', '2', '3', '4']  id= 1314353803840

# refList1 wird global verändert!  
# call by reference
# wenn man das nicht will, macht man ein neues Objekt und kopiert den Inhalt


"""
Kommandozeilen-Parameter
"""
import sys
for Argument in sys.argv:
    print(Argument)
    
# Aufruf Skript: python test.py eins zwei
# Ausgabe 'eins', 'zwei'

# weiter 14.11

"""
Variable Anzahl an Parameter
"""
def variableParameter(*x):
    print(x)
variableParameter() # ()
variableParameter(34, "String") # (34, 'String')

def variableStaedte(stadt, *andere):
    print(stadt, andere)
variableStaedte("Berlin") # Berlin ()
variableStaedte("Berlin","Frankfurt") # Berlin ('Frankfurt',)

# vereinzeln von Listen
def vereinzeln(x,y,z):
    print(x,y,z)
einzelneListe = (47,11,12)
vereinzeln(*einzelneListe) # 47 11 12

# doppelte Sternchen
def doppelt(**args):
    print(args)
doppelt() # {}
doppelt(de="deutsch", en="englisch") # {'de': 'deutsch', 'en': 'englisch'}

def foo(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
foo(42,43,x=17,y="Hallo",z=[3,8,9])
# args:  (42, 43)
# kwargs:  {'x': 17, 'y': 'Hallo', 'z': [3, 8, 9]}




    





