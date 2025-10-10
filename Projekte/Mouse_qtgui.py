import sys
import pyautogui
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QDesktopWidget
from PyQt5.QtCore import QTimer

# Hauptklasse für das Fenster
class MainWindow(QWidget):
    click_count = 0 # static variable

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setGeometry(100, 100, 300, 150)

        # Bildschirmgröße ermitteln und Fenster zentrieren (für PyQt5)
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())

        # Layout erstellen
        layout = QVBoxLayout()

        # Labels setzen
        self.label = QLabel("")
        layout.addWidget(self.label)
        self.timer_label = QLabel("Zeit: 00:00")
        layout.addWidget(self.timer_label)

        # Button hinzufügen
        self.button = QPushButton("Klicke mich")
        self.button.setFixedHeight(50)
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button)

        # Layout setzen
        self.setLayout(layout)

        #Timer für automatisierten Klick
        self.timer = QTimer()
        self.timer.timeout.connect(self.perform_automate_click)
        self.timer.start(5000) # click every 5 seconds

        # Zeit-Stoppuhr starten
        self.elapsed_seconds = 0

        # Zweiter Timer für die Stoppuhr (1 Sekunde Takt)
        self.stopwatch_timer = QTimer()
        self.stopwatch_timer.timeout.connect(self.update_stopwatch)
        self.stopwatch_timer.start(1000) # zählt jede Sekunde hoch

    def update_stopwatch(self):
        self.elapsed_seconds += 1
        minutes = self.elapsed_seconds // 60
        seconds = self.elapsed_seconds % 60
        self.timer_label.setText(f"Zeit: {minutes:02d}:{seconds:02d}")

    # Wenn Button geklickt wird
    def on_button_click(self):
        MainWindow.click_count += 1
        self.label.setText(f"Geklickt: {MainWindow.click_count}x")
        self.button.setStyleSheet("background-color: #1cff59;")

        # Nach 200 ms zurücksetzen
        QTimer.singleShot(200, lambda: self.button.setStyleSheet(""))
        

    def perform_automate_click(self):
        # Koordinaten des Buttons ermitteln
        #center = self.button.rect().center()
        #global_pos_center = self.button.mapToGlobal(center)

        button_rect = self.button.rect()
        global_top_left = self.button.mapToGlobal(button_rect.topLeft())

        button_width = self.button.width()
        button_height = self.button.height()

        #print(f"Button Position (Top-Left): {global_top_left}")
        #print(f"Button Size: Width={button_width}, Height={button_height}")

        # Zufällige X-Abweichung
        random_x = random.randint(5, button_width - 5)  # 5px Puffer links/rechts
        random_y = random.randint(5, button_height - 5)

        # Zielposition berechnen
        target_x = global_top_left.x() + random_x
        target_y = global_top_left.y() + random_y

        #print(f"[DEBUG] Klick bei x={target_x}, y={target_y}")

        # Maus bewegen und klicken
        pyautogui.moveTo(target_x, target_y)
        pyautogui.click()

# Start der Anwendung
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
