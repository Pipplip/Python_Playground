import sqlite3

connection = sqlite3.connect("test.db")
zeiger = connection.cursor()

''' 1 - einzelner Eintrag '''
nachname   = "Schiller"
vorname    = "Friedrich"
geburtstag = "10.11.1759"

#zeiger.execute(""" INSERT INTO personen VALUES (?,?,?) """,(vorname, nachname, geburtstag))


''' 2 - mehrere Einträge '''
beruehmtheiten = [('Georg Wilhelm Friedrich', 'Hegel', '27.08.1770'), 
                  ('Johann Christian Friedrich', 'Hölderlin', '20.03.1770'), 
                  ('Rudolf Ludwig Carl', 'Virchow', '13.10.1821')]

zeiger.executemany(""" INSERT INTO personen VALUES (?,?,?) """, beruehmtheiten)

connection.commit()
connection.close()