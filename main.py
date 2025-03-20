from PySide6 import QtWidgets, QtCore, QtMultimedia, QtGui
from resource_ui import Ui_Form
import os

class ListMusics:
    def __init__(self):
        self.paths = []
        self.names = []
        self.current_index = None

    def load(self, paths):
        new = []
        for path in paths:
            if path not in self.paths:
                self.paths.append(path)
                filename = os.path.basename(path)
                self.names.append(filename)
                new.append(filename)
        return new
    
    def get_current_path(self):
        return self.paths[self.current_index]

    def isempty(self):
        return len(self.names) == 0
    

class Player(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # icons
        self.play_icon = QtGui.QIcon(':/image/play-button-arrowhead.png')
        self.pause_icon = QtGui.QIcon(':/image/pause.png')

        # player
        self.player = QtMultimedia.QMediaPlayer()
        self.audio_output = QtMultimedia.QAudioOutput()
        self.audio_output.setVolume(1)
        self.player.setAudioOutput(self.audio_output)
        self.player.durationChanged.connect(self.set_duration_slider)

        # timer
        timer = QtCore.QTimer(self)
        timer.start(1000)
        timer.timeout.connect(self.update_play_slider)

        # main slider
        self.ui.main_slider.sliderMoved.connect(self.set_position)

        # volume slider
        self.ui.volume_slider.setRange(0, 100)
        self.ui.volume_slider.setValue(100)
        self.ui.volume_slider.valueChanged.connect(self.set_volume)

        # list
        self.list_musics = ListMusics()
        self.ui.add_button.clicked.connect(self.select_files)
        self.ui.playlist.currentRowChanged.connect(self.selected_changed)
        self.ui.playlist.doubleClicked.connect(self.play_or_pause)

        # play button
        self.ui.play_button.clicked.connect(self.play_or_pause)

        # next button
        self.ui.next_button.clicked.connect(self.next_song)

        # back button
        self.ui.back_button.clicked.connect(self.previous_song)

    def play_new(self, new_music_index):
            self.list_musics.current_index = new_music_index 
            path = self.list_musics.get_current_path()
            self.player.setSource(QtCore.QUrl.fromLocalFile(path))
            self.player.play()
            self.ui.play_button.setIcon(self.pause_icon)
            self.ui.playlist.setCurrentRow(new_music_index)

    def next_song(self):
        if self.list_musics.current_index is None: return
        next_index = (self.list_musics.current_index + 1) % len(self.list_musics.paths)
        self.play_new(next_index)

    def previous_song(self):
        if self.list_musics.current_index is None: return
        next_index = (self.list_musics.current_index - 1) % len(self.list_musics.paths)
        self.play_new(next_index)

    def selected_changed(self):
        if self.player.isPlaying():
            if self.list_musics.current_index == self.ui.playlist.currentRow():
                self.ui.play_button.setIcon(self.pause_icon)
            else:
                self.ui.play_button.setIcon(self.play_icon)

    def set_position(self, position):
        if (self.list_musics.current_index is not None):
            self.player.setPosition(position)

    def set_volume(self, value):
        self.audio_output.setVolume(value / 100)

    def set_duration_slider(self, duration):
        self.ui.main_slider.setRange(0, duration)

    def update_play_slider(self):
        if (self.list_musics.current_index is not None) and self.player.isPlaying():
            self.ui.main_slider.setValue(self.player.position())


    def play_or_pause(self):
        if self.list_musics.isempty(): return
        if self.player.isPlaying():
            if self.list_musics.current_index == self.ui.playlist.currentRow():
                self.player.pause()
                self.ui.play_button.setIcon(self.play_icon)
            else:
                self.play_new(self.ui.playlist.currentRow())
        else:
            if self.list_musics.current_index == self.ui.playlist.currentRow():
                self.player.play()
                self.ui.play_button.setIcon(self.pause_icon)
            else:
                self.play_new(self.ui.playlist.currentRow())

    def select_files(self):
        filenames = QtWidgets.QFileDialog.getOpenFileNames(None, 'Выберите аудио файлы', "", "Audio Files (*.mp3 *.wav *.ogg)")
        for filename in self.list_musics.load(filenames[0]):
            self.ui.playlist.addItem(" " * 4 + filename)


app = QtWidgets.QApplication([])
window = Player()
window.show()
app.exec()


