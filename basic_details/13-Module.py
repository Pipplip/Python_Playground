"""
Module
komplexes System in selbstständige Einheiten aufteilen

in Python:
Bibliotheken oder lokale Module(nur für ein Programm verfügbar)

Einbindung mit import

Suchreihenfolge für Module:
1. zuerst wird im aktuellen Verzeichnis nach dem Modul gesucht
2. PYTHONPATH
3. Installationspfad von Python

Pakete = Anzahl an mehrerer Module
Wie macht man Paket? 
1. Unterordner in einem Verzeichnis anlegen, in dem Python die Module erwartet
2. __init__.py anlegen (kann leer sein oder Initialiserungscode enthalten)
z.B. from TestPaket import a,b

"""
import math, random
print(math.pi) # 3.141592653589793

# komletten Namensraum einbinden
from math import *
print(sin(1)) # 0.8414709848078965
# anstatt math.sin(1)


# eigenen Namensraum benennen
import math as myMath
print(myMath.pi)


# Liste der Module bekommen
import sys
print(sys.builtin_module_names)
#print(dir(sys))

import basic_details.TestModul as TestModul
x = 2
y = TestModul.malZwei(x)
print(y)

# Pakete
import TestPaket
TestPaket.a.a()