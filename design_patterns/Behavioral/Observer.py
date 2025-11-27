"""
Objekte (Observer) registrieren sich bei einem anderen Objekt (Subject), um benachrichtigt zu werden, wenn sich dessen Zustand ändert.
Dies ermöglicht eine lose Kopplung zwischen dem Subject und den Observers.
"""
# ===== Subject (das beobachtete Objekt) =====
class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = None

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value
        self.notify_observers()


# ===== Observer (Beobachter) =====
class TemperatureDisplay:
    def update(self, temperature):
        print(f"Temperaturanzeige: Die aktuelle Temperatur ist {temperature}°C")

class PhoneApp:
    def update(self, temperature):
        print(f"Smartphone App: Temperatur-Update! {temperature}°C")

# ===== Beispielhafte Nutzung ===== 
if __name__ == "__main__":
    weather_station = WeatherStation()

    display = TemperatureDisplay()
    phone_app = PhoneApp()

    weather_station.register_observer(display)
    weather_station.register_observer(phone_app)

    weather_station.temperature = 25
    weather_station.temperature = 30

    weather_station.remove_observer(phone_app)

    weather_station.temperature = 28