"""
Empfohlen wird das pickle-Modul

Objekte werden serialisert abgelegt.
dump(obj, file, protocol=None, *, fix_imports=True) -> None

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

# print(s["city"]) # auslesen aus der shelve

# ------------------------------

# Bibliothek
tele = shelve.open("MyShelveBib")
tele["Mike"] = {"name":"Mike", "phone":"1234"}
tele["Eve"] = {"name":"Eve", "phone":"7866"}

print(tele["Eve"]["phone"]) # 7866