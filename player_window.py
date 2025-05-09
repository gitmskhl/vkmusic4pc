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

        self.saved_volume = 50 
        self.ui.pushButton_4.clicked.connect(self.addFiles)
        
        self.player = QtMultimedia.QMediaPlayer()
        self.audiooutput = QtMultimedia.QAudioOutput()
        self.audiooutput.setVolume(1)
        self.player.setAudioOutput(self.audiooutput)

        self.ui.verticalSlider.setValue(100)
        self.ui.verticalSlider.sliderMoved.connect(self.volume)
        self.ui.verticalSlider.sliderMoved.connect(self.volume_off)
        self.ui.pushButton_8.clicked.connect(self.volume_off)
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.moveSlider)
        
        self.ui.pushButton_7.clicked.connect(self.play)
        self.ui.horizontalSlider.sliderMoved.connect(self.musicMoved)

        self.fileNames = []

    def addFiles(self):
        fileNames = QFileDialog.getOpenFileNames(None, 'Выберите файл', '', 'Audio Files (*.mp3 *.wav *.ogg)')
        for i in fileNames[0]:
            self.ui.listWidget.addItem(os.path.basename(i))
            self.fileNames.append(i)


    def play(self, is_pause = True):
        if is_pause == True:
            # не оч понял, зачем еще раз проверять одно и тоеж
            if self.player.playbackState() == QtMultimedia.QMediaPlayer.PausedState:
                self.player.play()
            else: # тут же наоборот чекается, что музыка играла, значит ее надо остановить, а ниже она включается
                idx = self.ui.listWidget.currentRow()
                fileName = self.fileNames[idx]
                self.player.setSource(QtCore.QUrl.fromLocalFile(fileName))
                self.player.play()
                
                self.ui.horizontalSlider.setRange(0, self.player.duration())
                self.timer.start(10)
        else:
            self.player.pause()
            self.timer.stop() # это вроде функция, тут было self.timer.stop
            self.player.setPosition(self.player.position())  # зачем?
    

    def volume(self, newValue=None):
        if newValue is not None:
            self.audiooutput.setVolume(newValue/100)
        return self.audiooutput.volume() * 100


    def volume_off(self, is_off=False):
        if is_off:
            self.saved_volume = self.volume()  
            self.volume(0) 
        else:
            self.volume(self.saved_volume)
    

    def moveSlider(self):
        self.ui.horizontalSlider.setValue(self.player.position())


    def musicMoved(self, pos):
        self.player.setPosition(pos)
    