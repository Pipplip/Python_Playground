"""
Systemnahe Software wie z.B. das sys Modul fungiert als Abstraktionsschicht zwischen
der Anwendung, dem Python-Programm und dem Betriebssystem

Shell trennt Betreibsystemkern vom Benutzer und bietet ihm Funktionen an, um mit dem Kern zu
kommzunizieren.

Das wichtigste Python Modul ist das os-Modul

"""

# Bsp 1: Zugriffsrechte einer Datei lesen
import os
info = os.stat("lorem.txt")
print(type(info))
print(info)

# Umgebungsvariablen
print(os.getenv("USER"))


# os.abort() # abbrechen des Interpreters

# os.access(path, mode) - prüft welche Rechte das laufende P-Programm für den Path hat
# mode (optional): os.F_OK (prüft ob Pfad existiert), os.R_OK (read path allowed?)
# os.W_OK (write path allowed?), os.X_OK (Pfad ausführbar?)

# chdir(path) - Arbeitsverzeichnis wird geändert
#print(os.getcwd()) # C:\Users\Philipp Becker\Desktop\Einführung in P\Code
#os.chdir("C:/Users/Philipp Becker")
#print(os.getcwd()) # C:\Users\Philipp Becker

# os.chmod(path, mode) - Zugriffsrechte einer Datei/Pfad ändern

# os.chown(path, uid, gid) - ändern der Benutzer und Gruppen-Id

# os.chroot(path) - setzen des root Verzeichnisses

# os.extsep - Attribut mit Wert des Separators

# os.get_exec_path(env=None) - Liefert die Liste der Verzeichnisse, die zur Ausführung eines Programms durchsucht werden
# entspricht der PATH Werte

# os.getcwd() - Liefert aktuelle Arbeitsverzeichnis in Unicode-String

# os.getcwdb() - Arbeitsverzeichnis in Byte-String

# os.getgid / getuid 

# os.getgroups - Liste der Gruppen des aktuellen Prozesses

# os.getloadavg() - liefert Anzahl der Prozesse in Systemwarteschlange

# os.getlogin () - liefert login Name

# os.getpgid(pid) - Prozess-Gruppen-Id des Prozesses

# os.getpgrp() Gruppen-ID Prozess

# os.getpid() - Prozess-ID des laufenden Prozesses

# os.getppid() - Id Elternprozess

# os.listdir("/home/bernd/Documents") oder listdir() - wie dir in windows

# os.mkdirs(path[, mode])
#if os.path.isdir("x1")==False:
#    os.mkdirs("x1", 0755)

# os.removedirs(path)

# rename(src, dst)

# Baumstruktur ausgeben / Dateisystem rekursiv ausgeben
for path in os.walk("TestPaket"):
    print(path)

# os.sep - Pfad-Trennsymbol
os.chdir("C:"+os.sep+"Users"+os.sep+"Philipp Becker")

# viele viele mehr...