# main.py
import sys
from PySide6.QtWidgets import QApplication
from player_window import PlayerWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlayerWindow()
    sys.exit(app.exec())