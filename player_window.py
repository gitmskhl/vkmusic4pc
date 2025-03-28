from PySide6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QTextEdit, QVBoxLayout, QMainWindow, QDialog, QFileDialog
from interface_ui import Ui_Dialog
import os
from PySide6 import QtMultimedia, QtCore

class PlayerWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.ui.pushButton_4.clicked.connect(self.addFiles)
        self.player = QtMultimedia.QMediaPlayer()
        self.audiooutput = QtMultimedia.QAudioOutput()
        self.audiooutput.setVolume(1)
        self.player.setAudioOutput(self.audiooutput)
        self.ui.pushButton_7.clicked.connect(self.play)
        self.fileNames = []
    def addFiles(self):
        fileNames = QFileDialog.getOpenFileNames(None, 'Выберите файл', '', 'Audio Files (*.mp3 *.wav *.ogg)')
        for i in fileNames[0]:
            print(i)
            self.ui.listWidget.addItem(os.path.basename(i))
            self.fileNames.append(i)
    def play(self):
        idx = self.ui.listWidget.currentRow()
        fileName = self.fileNames[idx]
        self.player.setSource(QtCore.QUrl.fromLocalFile(fileName))
        self.player.play()

        