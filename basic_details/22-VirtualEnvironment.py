'''
Eigene Python-Projekte importieren meist 3rd Party libraries in einer bestimmten Version.
Da sich die 3rd Party libraries mit der Zeit aber ändern, kann es passieren,
dass der eigene Code nicht mehr funktioniert, weil sich z.B. Aufrufe in der 3rd Party Lib geändert haben.
Um immer einen feste Abhängigkeit in einem Projekt zu haben benutzt man virtuelle Umgebungen.

Jede virtuelle Umgebung hat:
1) eine bestimmte Python Version z.B. 3.9.1
2) Ordner mit den 3rd Party Libs

Vorgehen:
1) Erstelle ein Verzeichnis, in dem das Projekt liegen soll
2) NAvigiere in der Konsole zum Verzeichnis und erstelle eine virtuelle Umgebung:
    - mkdir myProjectName
    - wenn global schon Python installiert ist (Systemvariable) folgendes eingeben:
    - python --version (installierte Version vielleicht erstmal prüfen)
    - python3 -m venv /path/to/new/virtual/environment/myProjectName
3) virtuelle Umgebung aktivieren
    - wechsle in Konsole in Projekt-Verzeichnis
    - cmd.exe: C:\> <venv>\Scripts\activate.bat
    - PS: PS C:\> <venv>\Scripts\Activate.ps1
4) Ist die virtuelle Umgebung aktiv, kann man über pip Bibliotheken laden
    Diese werden dann nur in der virt. Umgebung gespeichert
5) Im Verzeichnis der virt. Umgebung eine requirements.txt anlegen und Abhängigkeiten eintragen
z.B. flask==1.0.0
     requests==2.1.2
     gunicorn // ohne Verion, installiert die neueste Bibliothek

Mit "pip install -rv requirements.txt" werden alle Bibliotheken geladen (wenn man das Projekt z.B. weitergibt und der User es einrichtet)

6) deaktivieren kann man die virt. Umgebung mit deactivate in Scripts Verzeichnis

'''