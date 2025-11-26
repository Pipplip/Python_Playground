"""

"""
# Alle Funktionen fuer Strings
# print(dir(str))

example = "The god of the world's leading religion. The chief temple is in the holy city of New York."

# lower/upper case
upper = example.upper()
lower = example.lower()
print(upper)
print(lower)

# Split
#print(example.split()) # split bei Leerzeichen

# csv Datei einlesen und bei ; splitten
fh = open("testCSV.csv", encoding="iso-8859-1")

for address in fh:
        address = address.strip()
        (lastname, firstname, city, phone) = address.split(';')
        print(firstname + " " + lastname+", "+city+", "+phone)

# max-split
print(example.split(None, 2)) # splitted die ersten 2 Strings, der Rest ist ein String
# ["The", "god", "of the ..."]

# split lines
# split nach einem Zeilentrenner "\r\n" in Windows und "\n\r" in Unix/Mac
win = "line1\nline2\n\rline3\r\nline4\rline5\n"
print(win.splitlines())
#['line1', 'line2', '', 'line3', 'line4', 'line5']

# partition: String an erster Stelle von l nach r aufspalten
parti = "Eine Katze, die jagt, hungert nicht!"
print(parti.partition(","))
# ('Eine Katze', ',', ' die jagt, hungert nicht!')


# Join: Strings aneinanderketten
languages = ["Python", "Java", "C"]
print("-".join(languages)) # Python-Java-C

# Substrings: Achtung case sensitiv
# in / not in
print("corner" in example) # False

print(example.find("lead")) # 23

print(example.index("lead")) # 23
print(example.index("lead")==example.find("lead")) # True

# Anzahl an Substrings
print(example.count("of")) # 2


# replace
ch = "Drei Chinesen mit dem Kontrabass"
ch = ch.replace("e", "a")
print(ch)

# stripping: ähnlich wie trim() in Java
strips = "\t \n\rMorgen kommt der Weihnachtsmann \t\n"
print(strips.strip())

plz = "690343 Frankfurt"
plz = plz.strip("0123456789 ")
print(plz) # 'Frankfurt'

# ausrichten: Auffuellen mit Leerzeichen
f = "Hallo"
center = f.center(6, "e") # 6=max Länge von Ergebnis, "e" fill, kann weggelassen werden, dann wird automatisch Leerzeichen eingefügt
print(center) # Halloe

center = f.center(4)
print(center) # Hallo, weil max Länge kleiner als f ist

# isalnum / prüft ob nur Zahlen
for word in ("mp3", "Hallo", "hello", "343", "767.43"):
    print("%6s : %s" % (word, word.isalnum()))

    # mp3 : True
    # Hallo : True
    # hello : True
    # 343 : True
    # 767.43 : False


# s.isalpha() = True, wenn alle Zeichen in s Buchstaben sind.
# s.isdigit() = True, wenn alle Zeichen in s Ziffern sind.
# s.islower() = True, wenn alle Buchstaben in s Kleinbuchstaben sind
# s.isupper() = True, wenn alle Buchstaben in s Großbuchstaben sind.
# s.isspace() = True, wenn alle Zeichen in s Whitespaces sind
# s.istitle() = True, wenn alle Wörter in s groß geschrieben sind