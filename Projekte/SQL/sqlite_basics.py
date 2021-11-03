import sqlite3

''' https://www.python-lernen.de/sqlite-datenbank-auslesen.htm '''

connection = sqlite3.connect("test.db")
zeiger = connection.cursor()

sql_anweisung = """
CREATE TABLE IF NOT EXISTS personen (
vorname VARCHAR(20), 
nachname VARCHAR(30), 
geburtstag DATE
);"""

zeiger.execute(sql_anweisung)
connection.commit()
connection.close()

'''
    1 - Verbindung zur Datenbank herstellen
    2 - Cursor-Objekt (zum Zugriff auf die Datenbank)
    3 - SQL-Query übergeben
    4 - commit: wir bestätigen der Datenbank, dass wir die SQL-Anweisung wirklich ausführen lassen wollen
    5 - Schließen der Datenbankverbindung (Ordnung muss sein)

'''