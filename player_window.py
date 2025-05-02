from PySide6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QTextEdit, QVBoxLayout, QMainWindow, QDialog, QFileDialog, QSlider
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
        self.ui.verticalSlider.setValue(100)
        self.ui.verticalSlider.sliderMoved.connect(self.volume)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.moveSlider)
        self.player.setAudioOutput(self.audiooutput)
        self.ui.pushButton_7.clicked.connect(self.play)
        self.ui.horizontalSlider.sliderMoved.connect(self.musicMoved)
        self.fileNames = []
        self.ui.horizontalSlider.mousePressEvent = self.mousePressEvent
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
        self.ui.horizontalSlider.setRange(0, self.player.duration())
        self.timer.start(10)
    def volume(self, newValue):
        self.audiooutput.setVolume(newValue/100)
    def moveSlider(self):
        self.ui.horizontalSlider.setValue(self.player.position())
    def musicMoved(self, pos):
        self.player.setPosition(pos)
    def mousePressEvent(self, event):
        value = self.ui.horizontalSlider.minimum() + ((self.ui.horizontalSlider.maximum() - self.ui.horizontalSlider.minimum()) * event.position().x()) / self.ui.horizontalSlider.width()
        self.ui.horizontalSlider.setValue(int(value))
        self.player.setPosition(int(value))
        event.accept()
        QSlider.mousePressEvent(event)



        

        