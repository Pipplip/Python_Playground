from enum import Enum

"""
Wenn viele verschiedene Objekte erstellt werden müssen, ohne die genaue Klasse der zu erstellenden Objekte anzugeben,
kann das Factory-Muster verwendet werden. Hier ist ein einfaches Beispiel, das eine Factory zur Erstellung verschiedener Transportmittel implementiert.

Die Logik der Objekterzeugung wird ausgelagert, sodass der Client-Code nicht wissen muss, welche konkreten Klassen verwendet werden.
Der Code ist flexibel für neue Objekttypen (open/closed principle) und fördert die lose Kopplung.

Abstract Factory Muster verwenden, wenn man Produktfamilien (Zusammengehörige Klassen) erstellen möchte.
Das normale Factory Muster wird verwendet, wenn man einzelne Produkte erstellen möchte.
"""

# ===== Enum für Transporttypen =====
class TransportType(Enum):
    CAR = "car"
    BIKE = "bike"
    PLANE = "plane"

# ===== Konkrete Transportklassen =====
class Car:
    def move(self):
        return "Das Auto fährt auf der Straße."

class Bike:
    def move(self):
        return "Das Fahrrad wird auf dem Radweg gefahren."

class Plane:
    def move(self):
        return "Das Flugzeug fliegt am Himmel."
    
# ===== Factory =====
class TransportFactory:
    _registry = {
        TransportType.CAR: Car,
        TransportType.BIKE: Bike,
        TransportType.PLANE: Plane,
    }

    @staticmethod
    def create_transport(t: TransportType):
        try:
            return TransportFactory._registry[t]()
        except KeyError:
            raise ValueError(f"Transport-Typ {t} wird nicht unterstützt.")
        
# ===== Client Code =====
if __name__ == "__main__":
    car = TransportFactory.create_transport(TransportType.CAR)
    print(car.move())

    bike = TransportFactory.create_transport(TransportType.BIKE)
    print(bike.move())