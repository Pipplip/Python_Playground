"""
Eingaben

Eingabe wird immer als String interpretiert
Man kann aber dementprechend casten.

"""

eingabe = input("Ihre Eingabe? ")
print(eingabe)

# Eingabe casten
ein1 = int(input("Ihr Alter? "))
print(ein1)
print(type(ein1)) # <class 'int'>

# Eingabe von Listen
liste = eval(input("Liste? "))
# EIngabe z.B. ["rot","grün"]
print(liste)