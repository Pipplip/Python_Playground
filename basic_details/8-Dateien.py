"""
Dateien
lesen/schreiben

Datei = Daten + Kartei

Inhalt einer Datei ist aus einer eindimesionalen Anneinanderreihung von Bits,
die normalerweise in Byte-Blöcke zusammengefasst interpretiert werden.
Bytes erhalten erst durch Anwendungsprogramme und das Bestriebssystem eine Bedeutung.
"""

# Text aus Datei lesen
fobj = open("lorem.txt", "r")
for line in fobj:
    print(line.rstrip())
fobj.close()

# auf Datenstruktur speichern
lorem = open("lorem.txt").readlines()
print(lorem) # Liste, jeder Eintrag der Liste entspricht einer Zeile
# ['Lorem ipsum dolor sit amet, consetetur sadipscing elitr, \n', ...]

# in String speichern
loremString = open("lorem.txt").read()
print(loremString)



# Schreiben in eine Datei
input = open("lorem.txt", "r")
output = open("lorem2.txt", "w")
counter = 0
for line in input:
    counter += 1
    output_line = "{0:>3s} {1:s}\n".format(str(counter),line.rstrip())
    output.write(output_line)
input.close()
output.close()