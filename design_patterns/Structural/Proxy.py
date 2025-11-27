"""
Das Proxy-Pattern ist ein Structural Design Pattern, das ein Objekt vertretend steuert, also den Zugriff auf ein anderes Objekt kontrolliert
Praktisch wird es z.B. bei Lazy Loading, Zugriffskontrolle, Caching oder Remote-Proxies verwendet.
"""
# Beispiel: Bildanzeige mit Lazy Loading
from time import sleep

# ===== Real Subject =====
class RealImage:
    def __init__(self, filename):
        self.filename = filename
        self.load_image()

    def load_image(self):
        print(f"Lade Bild {self.filename} ...")
        sleep(1)  # Simuliert lange Ladezeit
        print(f"Bild {self.filename} geladen.")

    def display(self):
        print(f"Bild {self.filename} wird angezeigt.")


# ===== Proxy =====
class ProxyImage:
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()

# ===== Client-Code =====
if __name__ == "__main__":
    image = ProxyImage("test_image.jpg")

    # Bild wird erst geladen, wenn display() aufgerufen wird
    image.display()  # Erstes Mal: Bild wird geladen und angezeigt
    image.display()  # Zweites Mal: Bild wird nur angezeigt, kein Laden