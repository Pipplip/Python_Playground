"""
Alle Klassen in Python erben von Object
__init__ entspricht dem Konstruktor
__del__ entspricht einem Destruktor (werden selten benutzt, weil man sich um das Aufräumen nicht kümmern muss)
__str__ und _repr__ entspricht dem toString in Java. Wandelt Datentyp in Sting um.
Diese Methoden kann man ueberschreiben. Und bei print() wird diese Methode dann aufgerufen

name   -> public - ohne führende Unterstriche
_name  -> protected - Bedeutet soviel wie "sollte nicht verwendet werden"
__name -> private - von aussen nicht sichtbar/benutzbar

statische Attribute (static in Java) = Klassenattribute (Eigenschaften, die für die ganze Klasse gelten und nicht nur für ein Objekt)
Wird unter der Klassendefinition deklariert. Hier Gesetze(...) oder counter
Statische Methoden sind an eine Klasse gebunden und nicht an eine Instanz


"""
# from robots import Roboter # importieren einer Klasse Roboter von Datei robots.py

class Roboter:

    __counter = 0 # private static
    Gesetze = ("Ich bin ein Klassenattribut", "...")
    # Aufruf: print(Roboter.Gesetze)
    # print(Roboter.AnzahlRoboter())

    def __init__(self, name, baujahr): # entspricht dem Konstruktor: __init__ muss so bleiben
        self.name = name
        self.__baujahr = baujahr # Baujahr ist private
        type(self).__counter += 1

    def __del__(self): # Destruktor (kann man weglassen)
        print("Roboter wurde zerstört")
        type(self).__counter -= 1

    def SageHallo(self): # Methoden-Deklaration, statt self kann man auch this oder etwas anderes nehmen
        print("Hallo, ich bin " + self.name)

    def AendereName(self, name):
        self.name = name

    def GetName(self):
        return self.name

    def SetzeBaujahr(self, baujahr):
        self.__baujahr = baujahr

    @staticmethod
    def AnzahlRoboter():
        return Roboter.__counter

    
    # repr = Darstellung von Daten, aus dem String lässt sich wieder ein Objekt machen, bei str nicht
    # mit eval lässt sich daraus wieder eine Instanz machen
    def __repr__(self):
        return "Roboter (\"" + self.name + "\", "+ str(self.__baujahr) + ")"

    def __str__(self):
        return "Name: " + self.name



# main Aufrufe
if __name__ == "__main__":
    x = Roboter("Robo1", 2000)
    x.SageHallo()
    print(x) # repr oder str wird in KLasse gesucht und ausgegeben. Hier self.name
    neu = eval(repr(x))
    print(Roboter.AnzahlRoboter()) # 2
    del(neu)
    print(Roboter.AnzahlRoboter()) # 1
    print(Roboter.Gesetze)


"""
Properties
"""
class P:
    def __init__(self, x):
        self.__x = x

    def __getX(self):
        return self.__x

    x = property(__getX)

# main Aufrufe
p = P(200)
# print(p.__getX) # geht nicht, da __getX private
print(p.x)

"""
Vererbung
"""
class Person:
    def __init__(self, name, geburtsdatum):
        self.name = name
        self.geburtsdatum = geburtsdatum

    def __str__(self):
        return self.name + " " + self.geburtsdatum


class Angestellter(Person): # in Python können Klassen von mehreren Klassen erben z.B. class Angestellter(Person, Gattung)
    def __init__(self, name, geburtsdatum, personalnummer):
        Person.__init__(self, name, geburtsdatum) # super Aufruf
        # oder super().__init__(...)
        self.personalnummer = personalnummer

    def __str__(self):
        return super().__str__() + ", " + self.personalnummer


if __name__ == "__main__":
    x = Angestellter("Homer", "01.01.2000", "001")
    print(x) # Homer 01.01.2000, 001

"""
Mehrfachvererbung - Diamantenproblem
"""
class A:
    def m(self):
        print("m von A aufgerufen")

class B:
    def m(self):
        print("m von B aufgerufen")

class C(A):
    def m(self):
        print("m von C aufgerufen")

class D(B,C): # je nachdem in welcher Reihenfolge hier die Basisklassen aufgerufen werden, ändert sich die Ausgabe
    pass

if __name__ == "__main__":
    x = D()
    print(x.m()) # m von B aufgerufen


"""
# Lösung
"""
class A1:
    def m(self):
        print("m von A aufgerufen")

class B1(A1):
    def m(self):
        print("m von B aufgerufen")
        super().m()

class C1(A1):
    def m(self):
        print("m von C aufgerufen")

class D1(B1,C1):
    def m(self):
        print("m von D aufgerufen")
        super().m()
    
if __name__ == "__main__":
    x1 = D1()
    print("\nDiamantenproblem:\n")
    x1.m() # m von D aufgerufen, m von B aufgerufen, m von C aufgerufen