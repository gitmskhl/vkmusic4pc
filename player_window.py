# player_window.py
import os
from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, Qt, QTime

from interface_ui import Ui_Dialog

class PlayerWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # --- Инициализация плеера ---
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        # --- Состояние плеера ---
        self.playlist = []
        self.current_index = -1
        self.is_slider_pressed = False
        self.is_shuffled = False
        self.is_repeating = False

        # --- Алиасы для удобства ---
        self.add_files_button = self.ui.pushButton_4
        self.playlist_widget = self.ui.listWidget
        self.play_pause_button = self.ui.pushButton_7
        self.next_button = self.ui.pushButton
        self.prev_button = self.ui.pushButton_2
        self.mute_button = self.ui.pushButton_8
        self.shuffle_button = self.ui.pushButton_9
        self.repeat_button = self.ui.pushButton_10
        self.seek_slider = self.ui.horizontalSlider
        self.volume_slider = self.ui.verticalSlider
        self.track_label = self.ui.label
        self.time_label = self.ui.label_2

        self.setWindowTitle("Music Player")

        # --- Настройка UI по умолчанию ---
        self.volume_slider.setValue(75)
        self.audio_output.setVolume(0.75)
        self.track_label.setText("No track selected")
        self.time_label.setText("00:00 / 00:00")
        self.track_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # --- Подключение сигналов к слотам ---
        self.connect_signals()
        
        self.show()

    def connect_signals(self):
        # Кнопки
        self.add_files_button.clicked.connect(self.add_files)
        self.play_pause_button.clicked.connect(self.toggle_play_pause)
        self.next_button.clicked.connect(self.next_song)
        self.prev_button.clicked.connect(self.previous_song)
        self.mute_button.clicked.connect(self.toggle_mute)
        
        # Виджеты
        self.playlist_widget.itemDoubleClicked.connect(self.play_from_list)
        
        # Слайдеры
        self.volume_slider.valueChanged.connect(self.set_volume)
        self.seek_slider.sliderPressed.connect(self.slider_pressed)
        self.seek_slider.sliderReleased.connect(self.slider_released)
        self.seek_slider.sliderMoved.connect(self.seek_position)
        
        # Сигналы плеера
        self.player.positionChanged.connect(self.update_slider_position)
        self.player.durationChanged.connect(self.update_slider_range)
        self.player.mediaStatusChanged.connect(self.handle_media_status)
        self.player.playbackStateChanged.connect(self.update_play_pause_icon)

    def add_files(self):
        file_paths, _ = QFileDialog.getOpenFileNames(
            self, 'Выберите аудиофайлы', '', 'Audio Files (*.mp3 *.wav *.ogg *.flac)'
        )
        if file_paths:
            for path in file_paths:
                url = QUrl.fromLocalFile(path)
                if url not in self.playlist:
                    self.playlist.append(url)
                    self.playlist_widget.addItem(os.path.basename(path))
            
            # Если это первые добавленные треки, начинаем играть первый
            if self.current_index == -1 and self.playlist:
                self.current_index = 0
                self.play_media(self.current_index)

    def play_media(self, index):
        if 0 <= index < len(self.playlist):
            self.current_index = index
            self.playlist_widget.setCurrentRow(index)
            self.player.setSource(self.playlist[index])
            self.player.play()
            self.update_track_info()

    def toggle_play_pause(self):
        if not self.playlist:
            return

        if self.player.playbackState() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            # Если плеер остановлен или на паузе
            if self.current_index == -1:
                 self.play_media(0)
            else:
                 self.player.play()

    def next_song(self):
        if not self.playlist:
            return
        
        new_index = (self.current_index + 1) % len(self.playlist)
        self.play_media(new_index)

    def previous_song(self):
        if not self.playlist:
            return
            
        # Если трек играет дольше 3 секунд, перемотать на начало, иначе - на предыдущий
        if self.player.position() > 3000:
            self.player.setPosition(0)
        else:
            new_index = (self.current_index - 1 + len(self.playlist)) % len(self.playlist)
            self.play_media(new_index)

    def play_from_list(self, item):
        index = self.playlist_widget.row(item)
        self.play_media(index)

    def handle_media_status(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.next_song()

    def update_track_info(self):
        if self.current_index != -1:
            base_name = os.path.basename(self.playlist[self.current_index].toLocalFile())
            self.track_label.setText(f"Сейчас играет: {base_name}")

    def update_slider_position(self, position):
        if not self.is_slider_pressed:
            self.seek_slider.setValue(position)
        self.update_time_label(position, self.player.duration())

    def update_slider_range(self, duration):
        self.seek_slider.setRange(0, duration)
        self.update_time_label(self.player.position(), duration)

    def seek_position(self, position):
        self.player.setPosition(position)
        
    def slider_pressed(self):
        self.is_slider_pressed = True

    def slider_released(self):
        self.is_slider_pressed = False
        self.seek_position(self.seek_slider.value())

    def set_volume(self, value):
        self.audio_output.setVolume(value / 100.0)
        if value > 0:
            self.mute_button.setChecked(False)
            self.audio_output.setMuted(False)

    def toggle_mute(self):
        self.audio_output.setMuted(not self.audio_output.isMuted())
        self.mute_button.setChecked(self.audio_output.isMuted())

    def update_play_pause_icon(self, state):
        if state == QMediaPlayer.PlayingState:
            self.play_pause_button.setChecked(True)
        else:
            self.play_pause_button.setChecked(False)
            
    def update_time_label(self, position, duration):
        if duration == 0:
            self.time_label.setText("00:00 / 00:00")
            return

        pos_time = QTime(0, 0, 0).addMSecs(position)
        dur_time = QTime(0, 0, 0).addMSecs(duration)

        format_str = "mm:ss" if duration < 3600000 else "hh:mm:ss"
        
        self.time_label.setText(f"{pos_time.toString(format_str)} / {dur_time.toString(format_str)}")