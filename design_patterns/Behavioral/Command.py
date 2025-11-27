"""
Kapselt Befehle in Objekten, sodass sie parametriert, gespeichert und rückgängig gemacht werden können.
Nützlich bei z.B. Undo-Funktionalitäten oder bei der Implementierung von Warteschlangen für Befehle.
"""
# Beispiel Fernbedieung für Geräte
# ===== Command Interface =====
class Command:
    def execute(self):
        pass


# ===== Receiver (Geräte, die die Arbeit machen) =====
class Light:
    def turn_on(self):
        print("Das Licht ist eingeschaltet.")

    def turn_off(self):
        print("Das Licht ist ausgeschaltet.")


class Fan:
    def turn_on(self):
        print("Der Ventilator ist eingeschaltet.")

    def turn_off(self):
        print("Der Ventilator ist ausgeschaltet.")


# ===== Concrete Commands =====
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


class FanOnCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.turn_on()


class FanOffCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.turn_off()


# ===== Invoker (z. B. Fernbedienung) =====
class RemoteControl:
    def __init__(self):
        self._commands = {}

    def set_command(self, button_name, command):
        self._commands[button_name] = command

    def press_button(self, button_name):
        if button_name in self._commands:
            self._commands[button_name].execute()
        else:
            print(f"Kein Befehl für Button '{button_name}' gesetzt.")

# ===== Client Code =====
if __name__ == "__main__":
    # Receiver-Objekte
    light = Light()
    fan = Fan()

    # Command-Objekte
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    fan_on = FanOnCommand(fan)
    fan_off = FanOffCommand(fan)

    # Invoker-Objekt
    remote = RemoteControl()
    remote.set_command("Licht An", light_on)
    remote.set_command("Licht Aus", light_off)
    remote.set_command("Ventilator An", fan_on)
    remote.set_command("Ventilator Aus", fan_off)

    # Befehle ausführen
    remote.press_button("Licht An")
    remote.press_button("Ventilator An")
    remote.press_button("Licht Aus")
    remote.press_button("Ventilator Aus")