"""
Zusammenfassungen
"""

''' mehrzeiliger Kommentar '''
# einzelner Kommentar

"""
Variablen
"""
i = 42
j = 2.34
print(type(i)) # <class 'int'>
# Operatoren:
# (+) Summe a + b
# (-) Differenz a - b
# (*) Produkt a * b
# (/) Quotient a / b
# (//) ganzzahlige Division a // b (abgerundet)
# (%) Modulo a % b
# (abs) Betrag von a abs(a)
# (**) Potenzieren a^b

t = True
false = False

""" ++++++++++++++++++++++++++++++++++++++++++
Strings
"""
string1 = "Hallo"
print(string1[0]) # H
print(len(string1)) # 5

print(string1[1:5]) # slicing -> allo

""" ++++++++++++++++++++++++++++++++++++++++++
Listen [a,b,c]
Listen = veränderbar also z.B. liste[0] = 1
"""
l1 = [3,99,"Ein Text"]
l2 = [ 42, 65, [45, 89], 88 ]
print(l2[2]) # [45,89]

# prüfen ob Liste leer ist
if not l1:
    print("Liste ist leer")

# Listen kopieren
l3 = ["a","b","c","d"]
l4 = l3[:]
# verschachtelte Listen kopieren
from copy import deepcopy
l5 = ["a","b",["ac","ad"]]
l6 = deepcopy(l5)

# zip-Funktion - Matrix erstellen
z1 = [11, 12, 13]
z2 = [21, 22, 23]
z3 = [31, 32, 33]
T = zip(z1, z2, z3)
print(list(T)) # [(11,21,31), (12,22,32), (13,23,33)]


# Stapelspeicher (stack) für Listen: Vorstellbar wie ein Bücherregal
# Auf Stapel legen (push/append), nehmen (pop) und schauen was ganz oben liegt (peek)
#    append() oder '+': am Ende des Stapels hinzufügen - append bevorzugen, da performanter
#    insert(): an beliebige Stelle des Stapels hinzufügen
#    remove(): entfernen eines Elements
#    pop(): letzte Element nehmen und ausschneiden
#    pop(i): Element i nehmen und ausschneiden
#    extend(t): an eine Liste mehrere Elemente anhängen
#    index(): Gibt die Stelle des Elements im Stack zurück

# Sortierung
stack5 = [6,8,7,3,8,4]
print(sorted(stack5)) # [3, 4, 6, 7, 8, 8]

""" ++++++++++++++++++++++++++++++++++++++++++
Tupel (1,2,3,"Text")
Tupel = unveränderbar, z.B. tupel[0] = 1 -> Exception
Nur lesen erlaubt
"""
t1 = (3,99,"Ein Text")

""" ++++++++++++++++++++++++++++++++++++++++++
Dictionary
Entspricht einer Map in Java: key-value mapping
map = {"key1":"value1","key2":"value2"}
"""
map2 = {"key1" : "value1", "key2" : "value2", "key3" : "value3"}
map2["key3"] = "value3a"
map2.get("key1") # value1
"value1" in map2 # True

# nützliche Methoden:
# kopieren: map2.copy(), bei verschachtelter Dic. deepcopy
# dic.items() - liefert alle key.value Paare
# dic.keys()  - liefert alle keys
# dic.pop("key1") - löschen eines keys
# dic.setdefault() - add key-value Paar (nur wenn noch nicht vorhanden)
# dic.update({"key3":"value3"}) - Dic wird erweitert oder überschrieben

""" ++++++++++++++++++++++++++++++++++++++++++
Set: Mengen. Ein Element kann in einem Set nicht doppelt vorkommen
Veränderliche Objekte wie Listen sind als Sets nicht erlaubt

set = {'Stadt1','Stadt2'}
"""
set1 = {'Hamburg','Müchnen','Frankfurt'}
set2 = set(('Paris', 'Paris', 'Lyon'))

# Nützliche Methoden:
# set1.add('Stuttgart') - Elemente hinzufügen
# set.clear() - Set leeren
# set.copy()
# set1.difference(set2) - Differenz zweier Mengen (set1 - set2 geht auch)
# set1.difference_update(set2) - entfernt alle Elemente einer Menge aus einer anderen Menge, die gleich sind
# set.discard("Stuttgart") oder set.remove("Stuttgart") - entfernen eines Elements
# set1.intersection(set2) - Liefert Schnittmenge zweier Sets (gleiche Elemente)
# set1.isdisjoint(set2) - True, wenn zwei Sets keine übereinstimmende Einträge haben (also leere Schnittmenge)
# set1.issubset(set2) - True, wenn Untermenge von set1 in set2 vorhanden ist
# set1.issuperset(set2) - True, wenn Obermenge von set1 in set2 vorhanden ist, x > y x enthält mindestens ein Element von y

""" ++++++++++++++++++++++++++++++++++++++++++
Eingaben: Eingabe wird immer als String interpretiert. Casten möglich
"""
eingabe = input("Ihre Eingabe? ")
# Eingabe casten
ein1 = int(input("Ihr Alter? "))
print(ein1)
print(type(ein1)) # <class 'int'>

# Eingabe von Listen
liste = eval(input("Liste? "))
# EIngabe z.B. ["rot","grün"]
print(liste)

""" ++++++++++++++++++++++++++++++++++++++++++
Verzweigungen
"""
if a == b:
    print()
else:
    print()
# -----------
if c > d:
    print()
elif c == d:
    print()
else:
    print()

# Operatoren
# == -> 42 == 42 True, [1,2]==[1,2] True
# != -> 42 != 43 True, {1,2] != 17 True
# < / > -> 4 < 12 True, "Ti" < "Tisc" True
# <= / >= -> 4 <= 4 True
# and, or, not -> Verbinden von Verknüpfungen

""" ++++++++++++++++++++++++++++++++++++++++++
Schleifen (while, foreach)
"""
# while
i = 0
while i < 4:
    i += 1
    if i == 2:
        continue
    if i == 3:
        break

# foreach
languages = ["a","b"]
for lan in languages:
    print(lan)

""" ++++++++++++++++++++++++++++++++++++++++++
Datei = Daten + Kartei

Inhalt einer Datei ist aus einer eindimesionalen Anneinanderreihung von Bits,
die normalerweise in Byte-Blöcke zusammengefasst interpretiert werden.
Bytes erhalten erst durch Anwendungsprogramme und das Bestriebssystem eine Bedeutung.
"""
# Text aus Datei lesen
fobj = open("lorem.txt", "r")
for line in fobj:
    print(line.rstrip())
fobj.close()

# auf Datenstruktur speichern
lorem = open("lorem.txt").readlines()

# in String speichern
loremString = open("lorem.txt").read()

# Schreiben in eine Datei
input = open("lorem.txt", "r")
output = open("lorem2.txt", "w")
counter = 0
for line in input:
    counter += 1
    output_line = "{0:>3s} {1:s}\n".format(str(counter),line.rstrip())
    output.write(output_line)
input.close()
output.close()

""" ++++++++++++++++++++++++++++++++++++++++++
Funktionen
"""
def sayHello(name):
    """ function prints 'sayHello' """
    return "Hello " + name

# default Parameter, wenn beim Aufruf nichts übergeben wird
def sayHello2(name="everybody"):
    return "Hello" + name

# wenn man globale Variablen in einer Funktion benutzen will, muss man diese angeben
def f():
    global s
    print(s)

""" ++++++++++++++++++++++++++++++++++++++++++
Ausnahmebehandlung
"""
try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())

except IOError as err:
    (errno, strerror) = err.args
    print("I/O error ({0}): {1}".format(errno, strerror))
except ValueError:
    print("No valid int value.")
except:
    (type, value, traceback) = sys.exc_info()
    print("Type: ", type)
    print("Value: ", value)
    print("traceback: ", traceback)
finally:
    print("Ich werde immer ausgegeben.")

""" ++++++++++++++++++++++++++++++++++++++++++
Klassen

Alle Klassen in Python erben von Object
__init__ entspricht dem Konstruktor
__del__ entspricht einem Destruktor (werden selten benutzt, weil man sich um das Aufräumen nicht kümmern muss)
__str__ und _repr__ entspricht dem toString in Java. Wandelt Datentyp in Sting um.
Diese Methoden kann man ueberschreiben. Und bei print() wird diese Methode dann aufgerufen

name   -> public - ohne führende Unterstriche
_name  -> protected - Bedeutet soviel wie "sollte nicht verwendet werden"
__name -> private - von aussen nicht sichtbar/benutzbar

statische Attribute (static in Java) = Klassenattribute (Eigenschaften, die für die ganze Klasse gelten und nicht nur für ein Objekt)
Wird unter der Klassendefinition deklariert. Hier Gesetze(...) oder counter
Statische Methoden sind an eine Klasse gebunden und nicht an eine Instanz
"""

# from robots import Roboter # importieren einer Klasse Roboter von Datei robots.py
class Roboter:

    __counter = 0 # private static
    Gesetze = ("Ich bin ein Klassenattribut", "...")
    # Aufruf: print(Roboter.Gesetze)
    # print(Roboter.AnzahlRoboter())

    def __init__(self, name, baujahr): # entspricht dem Konstruktor: __init__ muss so bleiben
        self.name = name
        self.__baujahr = baujahr # Baujahr ist private
        type(self).__counter += 1

    def __del__(self): # Destruktor (kann man weglassen)
        print("Roboter wurde zerstört")
        type(self).__counter -= 1

    def SageHallo(self): # Methoden-Deklaration, statt self kann man auch this oder etwas anderes nehmen
        print("Hallo, ich bin " + self.name)

    def AendereName(self, name):
        self.name = name

    def GetName(self):
        return self.name

    def SetzeBaujahr(self, baujahr):
        self.__baujahr = baujahr

    @staticmethod
    def AnzahlRoboter():
        return Roboter.__counter

    
    # repr = Darstellung von Daten, aus dem String lässt sich wieder ein Objekt machen, bei str nicht
    # mit eval lässt sich daraus wieder eine Instanz machen
    def __repr__(self):
        return "Roboter (\"" + self.name + "\", "+ str(self.__baujahr) + ")"

    def __str__(self):
        return "Name: " + self.name



# main Aufrufe
if __name__ == "__main__":
    x = Roboter("Robo1", 2000)
    x.SageHallo()
    print(x) # repr oder str wird in KLasse gesucht und ausgegeben. Hier self.name
    neu = eval(repr(x))
    print(Roboter.AnzahlRoboter()) # 2
    del(neu)
    print(Roboter.AnzahlRoboter()) # 1
    print(Roboter.Gesetze)

# Vererbung
# class Angestellter(Person): # in Python können Klassen von mehreren Klassen erben z.B. class Angestellter(Person, Gattung)

""" ++++++++++++++++++++++++++++++++++++++++++
Persistente Speicherung
"""
import pickle
# Speichern
#cities = ["Berlin", "Amsterdam", "München"]
#fh = open("serializedData.pkl","wb")
#pickle.dump(cities, fh)
#fh.close

# laden
fo = open("serializedData.pkl","rb")
staedte = pickle.load(fo)
fo.close
print(staedte)

# Shelve - ähnlich wie ein Bücherregal
# Das Regal ist eine Datei und die Bücher sind unsere Daten
# Empfohlen bei Dictionaries
import shelve
s = shelve.open("MyShelve") # wenn es die Datei nicht gibt, wird diese angelegt
s["street"] = "main street"
s["city"] = "London"

for key in s:
    print(key)

s.close()


""" ++++++++++++++++++++++++++++++++++++++++++
Threads und Locks
MultiThreading = für GUIs, I/O. Shared memory. Python verwaltet Threading
Multiprocessing = eigener CPU Kern und Speicherbereich (schneller als Threading). System verwaltet Processing

ACHTUNG: wenn man Threads locked und alle auf einen anderen Thread warten hat man einen Deadlock

"""
import threading

class MyThread(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self) # Oberklasse von Thread aufrufen
        self.id = id
        self.name = name

    def run(self):
        lockMe.acquire() # blockiert bis der erste Thread fertig ist
        print("Starte ", self.id)
        print("Beende ", self.id)
        lockMe.release()

lockMe = threading.Lock()

t1 = MyThread(1,"t1")
t2 = MyThread(2,"t2")
t1.start()
t2.start()

# t1.join() # warten bis t1 fertig ist
# if t1.isAlive(): # gibt aus ob der Thread noch existiert
print("Beende Main")


""" ++++++++++++++++++++++++++++++++++++++++++
Umwandlung in exe Datei mit PyInstaller

Install: pip install pyinstaller
In Konsole pyinstaller datei.py

Zusätzlich:
pip install auto-py-to-exe

Danach in Console:
auto-py-to-exe
"""

""" ++++++++++++++++++++++++++++++++++++++++++
GUIs
tkinter - wird mit Python bereits geliefert, muss nicht extra installiert werden
"""
import tkinter as tk

root = tk.Tk()

w = tk.Label(root, text="Hello Tkinter!")
w.pack()

root.mainloop()
