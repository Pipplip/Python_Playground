"""
Erstellung einer einzigen Instanz einer Klasse (Singleton Pattern).
Auf diese Klasse kann global zugegriffen werden.

Klassischer Anwendungsfall: Konfigurationsmanager, Logger, Datenbankverbindung.

"""
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    

# Beispielverwendung
if __name__ == "__main__":
    singleton1 = Singleton()
    singleton2 = Singleton()

    print(singleton1 is singleton2)  # Ausgabe: True, beide Variablen verweisen auf dieselbe Instanz