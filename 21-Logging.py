"""
Logging
"""
import logging

'''
Es gibt 5 Loglevel:
- DEBUG (wird bei default in der Konsole nicht angezeigt)
- INFO (wird bei default in der Konsole nicht angezeigt)
- WARNING
- ERROR
- CRITICAL


Basic Einstellungen
'''
''' Loggen in der Konsole '''
# level = ab welchem Level geloggt werden soll
#logging.basicConfig(level=logging.DEBUG) 
#logging.debug('Jetzt wird debug in der Konsole angezeigt')


''' Loggen in einer Datei'''
# log in Datei speichern anstatt in der Konsole
logging.basicConfig(filename="msg.log", level=logging.DEBUG, filemode="w", format="%(asctime)s %(name)s - %(levelname)s - %(message)s")
logging.warning('Warning wird in einer Datei gespeichert')

name = "Name"
logging.warning("%s Variable wird geloggt", name)

''' Error Trace loggen '''
try:
    a = 10
    b = 0
    c = a/b
except Exception as e:
    logging.error("Exception: " + str(e), exc_info=True)

'''
Logger für Klassen oder Methoden
-> dann steht nicht root im log sondern die Klasse oder die Methode
'''
def f():
    logger = logging.getLogger("Funktionsname f()")
    logger.setLevel(logging.DEBUG)
    logger.debug("Log in der Funktion")

f()

'''
Filehandler
verwaltet eine neue Log-Datei (neben z.B. dem root Logger)
also Format, Dateiname etc. kann individuell geändert werden

Der root Logger (hier: msg.log) schreibt zusätzlich mit mit seinem eigenen Format
D.h. der root Logger loggt immer mit
'''
# lg ist mein neuer zusätzlicher Logger
lg = logging.getLogger("meinLogger")
lg.setLevel(logging.DEBUG)
filehandle = logging.FileHandler("logme.log")
form = logging.Formatter("%(asctime)s %(name)s - %(levelname)s - %(message)s")
filehandle.setFormatter(form)
lg.addHandler(filehandle)

lg.debug("Mein FileHandler Log")