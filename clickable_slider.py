# clickable_slider.py
from PySide6.QtWidgets import QSlider, QStyle
from PySide6.QtCore import Qt

class ClickableSlider(QSlider):
    def __init__(self, parent=None, byX=True):
        super().__init__(parent)
        self.byX = byX

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.orientation() == Qt.Horizontal:
                val = QStyle.sliderValueFromPosition(
                    self.minimum(), self.maximum(), event.pos().x(), self.width()
                )
            else:
                # Для вертикального слайдера позиция инвертирована
                val = self.maximum() - QStyle.sliderValueFromPosition(
                    self.minimum(), self.maximum(), event.pos().y(), self.height()
                )
            self.setValue(val)
            self.sliderMoved.emit(val) # Отправляем сигнал, чтобы перемотка сработала сразу
        super().mousePressEvent(event)