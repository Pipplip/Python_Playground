"""
Erstelle komplexe Objekte Schritt für Schritt und kontrolliert mit dem Builder-Entwurfsmuster.
"""
# ===== Produktklasse =====
class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.bacon = False

    def __str__(self):
        toppings = []
        if self.cheese:
            toppings.append("Cheese")
        if self.pepperoni:
            toppings.append("Pepperoni")
        if self.bacon:
            toppings.append("Bacon")
        return f"Pizza ({self.size}) with: {', '.join(toppings) if toppings else 'no toppings'}"
    
# ===== Builder-Klasse =====
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self  # ermöglicht Method-Chaining

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_bacon(self):
        self.pizza.bacon = True
        return self

    def build(self):
        return self.pizza
    
# ===== Verwendung des Builders =====
if __name__ == "__main__":
    builder = PizzaBuilder()
    pizza = (builder.set_size("Large")
                   .add_cheese()
                   .add_pepperoni()
                   .build())
    print(pizza)  # Ausgabe: Pizza (Large) with: Cheese, Pepperoni