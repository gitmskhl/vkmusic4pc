# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resource.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSlider, QWidget)
import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(660, 500)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 660, 500))
        self.widget.setStyleSheet(u"QListWidget {\n"
"	background-color: rgba(0, 0, 0, 100);\n"
"	border-top-left-radius: 30px;\n"
"	border-top-right-radius: 30px;\n"
"	padding: 10px 5px ;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"	color: rgb(255, 255, 255);\n"
"	padding: 5px 5px 5px 10px;\n"
"	height: 15px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"	background-color: rgba(255, 100, 0, 100);\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QSlider::groove {\n"
"	height: 5px;\n"
"	border-radius: 5px;	\n"
"	background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"\n"
"QSlider::handle {\n"
"	background-color: rgba(0, 0, 0, 200);\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	width: 10px;\n"
"	height: 10px;\n"
"	margin: -3px 0;\n"
"}\n"
"\n"
"QSlider::sub-page {\n"
"	background-color: rgba(0, 50, 200, 100);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(0,0,0, 50);\n"
"}\n"
"\n"
"\n"
"QPushButton#a"
                        "dd_button:hover {\n"
"	background-color: rgba(0,0,0, 0);\n"
"}")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 660, 500))
        self.label.setStyleSheet(u"border-image: url(:/image/Gemini_Generated_Image_f3aimyf3aimyf3ai.jpeg);")
        self.main_slider = QSlider(self.widget)
        self.main_slider.setObjectName(u"main_slider")
        self.main_slider.setGeometry(QRect(29, 430, 601, 20))
        self.main_slider.setOrientation(Qt.Horizontal)
        self.play_button = QPushButton(self.widget)
        self.play_button.setObjectName(u"play_button")
        self.play_button.setGeometry(QRect(290, 460, 88, 25))
        self.play_button.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/image/play-button-arrowhead.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.play_button.setIcon(icon)
        self.next_button = QPushButton(self.widget)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setGeometry(QRect(380, 460, 88, 25))
        self.next_button.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/image/next.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.next_button.setIcon(icon1)
        self.back_button = QPushButton(self.widget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(200, 460, 88, 25))
        self.back_button.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/image/back.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.back_button.setIcon(icon2)
        self.playlist = QListWidget(self.widget)
        self.playlist.setObjectName(u"playlist")
        self.playlist.setGeometry(QRect(35, 31, 591, 391))
        font = QFont()
        font.setPointSize(16)
        font.setBold(False)
        self.playlist.setFont(font)
        self.playlist.setStyleSheet(u"")
        self.volume_slider = QSlider(self.widget)
        self.volume_slider.setObjectName(u"volume_slider")
        self.volume_slider.setGeometry(QRect(530, 460, 101, 20))
        self.volume_slider.setOrientation(Qt.Horizontal)
        self.add_button = QPushButton(self.widget)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(40, 460, 41, 25))
        icon3 = QIcon()
        icon3.addFile(u":/image/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_button.setIcon(icon3)
        self.add_button.setIconSize(QSize(24, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.play_button.setText("")
        self.next_button.setText("")
        self.back_button.setText("")
        self.add_button.setText("")
    # retranslateUi

