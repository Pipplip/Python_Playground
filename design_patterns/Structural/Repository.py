"""
Das Repository-Pattern ist ein Design-Pattern aus der Datenzugriffsschicht, 
das die Datenzugriffe kapselt und eine abstrakte Schnittstelle zu einer Datenquelle bereitstellt. 
Praktisch wird es verwendet, um CRUD-Operationen von der Geschäftslogik zu trennen und den Code sauberer und testbarer zu machen.
"""
# Beispiel: Benutzer-Repository mit SQLite
# Vorteil: Trennung von Geschäftslogik und Datenzugriff.
import sqlite3

# ===== Entity =====
class User:
    def __init__(self, user_id, name, email):
        self.id = user_id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"


# ===== Repository =====
class UserRepository:
    def __init__(self, db_name="users.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)"
        )
        self.connection.commit()

    def add(self, user):
        self.cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)", (user.name, user.email)
        )
        self.connection.commit()
        user.id = self.cursor.lastrowid
        return user

    def get_by_id(self, user_id):
        self.cursor.execute("SELECT id, name, email FROM users WHERE id=?", (user_id,))
        row = self.cursor.fetchone()
        if row:
            return User(*row)
        return None

    def get_all(self):
        self.cursor.execute("SELECT id, name, email FROM users")
        rows = self.cursor.fetchall()
        return [User(*row) for row in rows]

    def update(self, user):
        self.cursor.execute(
            "UPDATE users SET name=?, email=? WHERE id=?", (user.name, user.email, user.id)
        )
        self.connection.commit()

    def delete(self, user):
        self.cursor.execute("DELETE FROM users WHERE id=?", (user.id,))
        self.connection.commit()

    def close(self):
        self.connection.close()

# ===== Beispielhafte Nutzung =====
if __name__ == "__main__":
    repo = UserRepository()

    # Benutzer hinzufügen
    user1 = repo.add(User(None, "Alice", "alice@example.com"))
    user2 = repo.add(User(None, "Bob", "bob@example.com"))

    # Alle Benutzer abrufen
    print(repo.get_all())

    # Benutzer aktualisieren
    user1.name = "Alice Updated"
    repo.update(user1)
    print(repo.get_by_id(user1.id))

    # Benutzer löschen
    repo.delete(user2)
    print(repo.get_all())

    repo.close()