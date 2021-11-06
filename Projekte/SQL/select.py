import sqlite3

connection = sqlite3.connect("test.db")
zeiger = connection.cursor()
zeiger.execute("SELECT * FROM personen")
inhalt = zeiger.fetchall()
#print(inhalt)
for entry in inhalt:
    print(f"{entry[0]} - {entry[1]} - {entry[2]}")
    #print(entry)

connection.close()