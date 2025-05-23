from PySide6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QTextEdit, QVBoxLayout, QMainWindow, QDialog, QFileDialog, QSlider
from interface_ui import Ui_Dialog
import os
from PySide6 import QtMultimedia, QtCore

class PlayerWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.saved_volume = 50
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.saved_volume = 50
        self.ui.pushButton_4.clicked.connect(self.addFiles)
        self.player = QtMultimedia.QMediaPlayer()
        self.audiooutput = QtMultimedia.QAudioOutput()
        self.audiooutput.setVolume(1)
        self.ui.verticalSlider.setValue(100)
        self.ui.verticalSlider.sliderMoved.connect(self.volume)
        self.ui.verticalSlider.valueChanged.connect(self.volume)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.moveSlider)
        self.player.setAudioOutput(self.audiooutput)
        self.ui.pushButton_7.clicked.connect(self.play)
        self.ui.horizontalSlider.sliderMoved.connect(self.musicMoved)
        self.fileNames = []
        self.ui.listWidget.itemDoubleClicked.connect(self.play_selected)
        self.current_index = -1

    def addFiles(self):
        fileNames = QFileDialog.getOpenFileNames(None, 'Выберите файл', '', 'Audio Files (*.mp3 *.wav *.ogg)')
        for i in fileNames[0]:
            if i not in self.fileNames:
                print(i)    
                self.ui.listWidget.addItem(os.path.basename(i))
                self.fileNames.append(i)
            else:
                print(f"Файл {i} уже был добавлен ранее")

    def play_selected(self):
        self.current_index = self.ui.listWidget.currentRow()
        if  self.current_index < len(self.fileNames):
             # Останавливаем текущее воспроизведение
            self.player.stop()
            # Очищаем текущий источник
            self.player.setSource(QtCore.QUrl.fromLocalFile(self.fileNames[self.current_index]))
            self.player.play()
            # Обновляем слайдер
            self.ui.horizontalSlider.setRange(0, self.player.duration())
            self.timer.start(10)
            

    def play(self, is_pause: True):
        if is_pause == True:
            if self.player.playbackState() == QtMultimedia.QMediaPlayer.PausedState:
                self.player.play()
            else:
                idx = self.ui.listWidget.currentRow()
                fileName = self.fileNames[idx]
                self.player.setSource(QtCore.QUrl.fromLocalFile(fileName))
                self.player.play()
                
                self.ui.horizontalSlider.setRange(0, self.player.duration())
                self.timer.start(10)
        else:
            self.player.pause()
            self.timer.stop
            self.player.setPosition(self.player.position()) 
    
    def volume(self, newValue=None):
        #if newValue is not None:
        self.audiooutput.setVolume(newValue/100)
        #return self.audiooutput.volume() * 100

    '''def volume_off(self, is_off=False):
        if is_off:
            self.saved_volume = self.volume()  
            self.volume(0) 
        else:
            self.volume(self.saved_volume)'''
    
    def moveSlider(self):
        if self.ui.horizontalSlider.active or self.ui.horizontalSlider.has_been_activated: 
            self.musicMoved(self.ui.horizontalSlider.value())
            self.ui.horizontalSlider.has_been_activated = False
            return
        self.ui.horizontalSlider.setValue(self.player.position())

    def musicMoved(self, pos):
        self.player.setPosition(pos)

    # def mousePressEvent(self, event):
    #     value = self.ui.horizontalSlider.minimum() + ((self.ui.horizontalSlider.maximum() - self.ui.horizontalSlider.minimum()) * event.position().x()) / self.ui.horizontalSlider.width()
    #     self.ui.horizontalSlider.setValue(int(value))
    #     self.player.setPosition(int(value))
    #     event.accept()
    #     global_pos = self.ui.horizontalSlider.mapToGlobal(self.ui.horizontalSlider.pos())
    #     print(global_pos)
    #     print(event.position().x())
        



        

        