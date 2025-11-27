from enum import Enum
from abc import ABC, abstractmethod

"""
Eine Abstract Factory ist ein Entwurfsmuster, das eine Schnittstelle zur Erstellung von Familien verwandter oder abhängiger Objekte bereitstellt,
ohne ihre konkreten Klassen anzugeben. Dieses Muster wird verwendet, wenn das System unabhängig von der Art der erstellten Objekte bleiben soll.
Es fördert die Konsistenz unter den Produkten einer Familie und erleichtert das Hinzufügen neuer Produktfamilien.
Hier ist ein Beispiel, das eine Abstract Factory zur Erstellung verschiedener Transportmittel und deren Motoren implementiert.
Also zusammengehörige Objekte werden zusammen erstellt.
Vorteile sind unter anderem die Einhaltung des Open/Closed-Prinzips und die Förderung der lose Kopplung.
Produkte können leicht ausgetauscht oder hinzugefügt werden, ohne den Client-Code zu ändern.

Abstract Factory Muster verwenden, wenn man Produktfamilien (Zusammengehörige Klassen) erstellen möchte.
Das normale Factory Muster wird verwendet, wenn man einzelne Produkte erstellen möchte.

Die Struktur umfasst:
- Enum für Transporttypen
- Abstrakte Produkte
- Konkrete Transport- und Engine-Klassen
- Abstrakte Fabrik
- Konkrete Fabriken
- Factory Provider
"""

# ===== Enum für Transporttypen =====
class TransportType(Enum):
    CAR = "car"
    PLANE = "plane"

# ===== Abstrakte Produkte =====
class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

# ===== Konkrete Transport- und Engine-Klassen =====
class Car(Transport):
    def move(self):
        return "Das Auto fährt."

class CarEngine(Engine):
    def start(self):
        return "Auto-Motor startet."

class Plane(Transport):
    def move(self):
        return "Das Flugzeug fliegt."

class JetEngine(Engine):
    def start(self):
        return "Jet-Motor startet."
    
# ===== Abstrakte Fabrik =====
class AbstractTransportFactory(ABC):

    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    @abstractmethod
    def create_engine(self) -> Engine:
        pass

# ===== Konkrete Fabriken =====
class CarFactory(AbstractTransportFactory):
    def create_transport(self) -> Transport:
        return Car()

    def create_engine(self) -> Engine:
        return CarEngine()


class PlaneFactory(AbstractTransportFactory):
    def create_transport(self) -> Transport:
        return Plane()

    def create_engine(self) -> Engine:
        return JetEngine()
    
# ===== Factory Provider =====
class FactoryProvider:
    factories = {
        TransportType.CAR: CarFactory,
        TransportType.PLANE: PlaneFactory,
    }

    @staticmethod
    def get_factory(t: TransportType) -> AbstractTransportFactory:
        try:
            return FactoryProvider.factories[t]()
        except KeyError:
            raise ValueError(f"Keine Factory für Typ {t} vorhanden.")
        
# ===== Client Code =====
if __name__ == "__main__":
    car_factory = FactoryProvider.get_factory(TransportType.CAR)
    car = car_factory.create_transport()
    car_engine = car_factory.create_engine()
    print(car.move())
    print(car_engine.start())

    plane_factory = FactoryProvider.get_factory(TransportType.PLANE)
    plane = plane_factory.create_transport()
    jet_engine = plane_factory.create_engine()
    print(plane.move())
    print(jet_engine.start())