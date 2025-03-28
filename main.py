from PySide6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QTextEdit, QVBoxLayout
from player_window import PlayerWindow
app = QApplication([])

window = PlayerWindow()
app.exec()
