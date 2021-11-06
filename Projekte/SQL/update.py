import sqlite3


def print_full_db(liste):
    for entry in liste:
        print(f"{entry[0]} - {entry[1]} - {entry[2]}")
    print("\n")

connection = sqlite3.connect("test.db")
zeiger = connection.cursor()
zeiger.execute("SELECT * FROM personen")
inhalt = zeiger.fetchall()
print_full_db(inhalt)

nachname   = "Schiller"
vorname    = "Johann Christoph Friedrich"

zeiger.execute("UPDATE personen SET vorname=? WHERE nachname=?", (vorname, nachname))
connection.commit()

zeiger.execute("SELECT * FROM personen")
inhalt = zeiger.fetchall()
print_full_db(inhalt)
connection.close()