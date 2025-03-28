# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1102, 739)
        Dialog.setStyleSheet(u"background-color: rgb(25, 25, 25);")
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(100, 0))
        self.frame.setMaximumSize(QSize(20, 16777215))
        self.frame.setStyleSheet(u"border: none;\n"
"background-color: rgb(43, 43, 43);\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(30)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 0, 9, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(25, 25))
        self.pushButton_5.setMaximumSize(QSize(25, 25))
        self.pushButton_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px\n"
"")

        self.verticalLayout_5.addWidget(self.pushButton_5, 0, Qt.AlignHCenter)

        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(25, 25))
        self.pushButton_6.setMaximumSize(QSize(25, 25))
        self.pushButton_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px\n"
"")

        self.verticalLayout_5.addWidget(self.pushButton_6, 0, Qt.AlignHCenter)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(25, 25))
        self.pushButton_4.setMaximumSize(QSize(25, 25))
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px\n"
"")

        self.verticalLayout_5.addWidget(self.pushButton_4, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setStyleSheet(u"border: none;\n"
"background-color: rgb(25, 25, 25);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 550))
        self.frame_4.setStyleSheet(u"border: none;\n"
"background-color: rgb(43, 43, 43);\n"
"border-radius: 10px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 50))
        self.frame_6.setMaximumSize(QSize(16777215, 100))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 32442))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_10 = QPushButton(self.frame_7)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(25, 25))
        self.pushButton_10.setMaximumSize(QSize(25, 25))
        self.pushButton_10.setStyleSheet(u"background-color: white;\n"
"border-radius: 5px\n"
"")

        self.horizontalLayout_6.addWidget(self.pushButton_10)

        self.pushButton_9 = QPushButton(self.frame_7)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(25, 25))
        self.pushButton_9.setMaximumSize(QSize(25, 25))
        self.pushButton_9.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"border-radius: 5px;\n"
"opacity: 0;\n"
"")
        icon = QIcon()
        icon.addFile(u":/butt/C:/Users/ivans/Downloads/Group 5.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/butt/C:/Users/ivans/Downloads/Group 5 (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_9.setIcon(icon)
        self.pushButton_9.setIconSize(QSize(23, 23))
        self.pushButton_9.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.pushButton_9)


        self.horizontalLayout_3.addWidget(self.frame_7)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(600, 30))
        self.frame_9.setMaximumSize(QSize(600, 16777215))
        self.frame_9.setStyleSheet(u"#horizontalSlider::groove{\n"
"background-color: rgb(193, 193, 193);\n"
"height: 3px;\n"
"border: none;\n"
"border-radius: 1px\n"
"}\n"
"#horizontalSlider::sub-page{\n"
"background-color: white;\n"
"height: 3px;\n"
"border: none;\n"
"border-radius: 1px\n"
"}\n"
"#horizontalSlider::handle{\n"
"background-color: white;\n"
"height: 5px;\n"
"width: 9px;\n"
"border: none;\n"
"border-radius: 4px;\n"
"margin: -3px 0px\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.pushButton_7 = QPushButton(self.frame_9)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(45, 45))
        self.pushButton_7.setMaximumSize(QSize(35, 35))
        self.pushButton_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"opacity: 0;\n"
"border-radius: 5px\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/butt/C:/Users/ivans/Downloads/Polygon 1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/butt/C:/Users/ivans/Downloads/Group 1 (5).png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QSize(30, 30))
        self.pushButton_7.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_7, 0, Qt.AlignHCenter)

        self.horizontalSlider = QSlider(self.frame_9)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.horizontalSlider)


        self.horizontalLayout_3.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"#verticalSlider::groove{\n"
"background-color: white;\n"
"width: 3px;\n"
"border: none;\n"
"border-radius: 1px\n"
"}\n"
"#verticalSlider::sub-page{\n"
"background-color: rgb(193, 193, 193);\n"
"height: 3px;\n"
"border: none;\n"
"border-radius: 1px\n"
"}\n"
"#verticalSlider::handle{\n"
"background-color: white;\n"
"height: 9px;\n"
"width: 9px;\n"
"border: none;\n"
"border-radius: 4px;\n"
"margin: 0px -3px\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_8 = QPushButton(self.frame_10)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(25, 25))
        self.pushButton_8.setMaximumSize(QSize(25, 25))
        self.pushButton_8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"border-radius: 5px;\n"
"opacity: 0\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/butt/C:/Users/ivans/Downloads/Group 1 (3).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/butt/C:/Users/ivans/Downloads/Group 3.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setIconSize(QSize(25, 25))
        self.pushButton_8.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.pushButton_8)

        self.verticalSlider = QSlider(self.frame_10)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMaximumSize(QSize(16777215, 50))
        self.verticalSlider.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_5.addWidget(self.verticalSlider)


        self.horizontalLayout_3.addWidget(self.frame_10)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.listWidget = QListWidget(self.frame_4)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"border: none;\n"
"background-color: rgb(63, 63, 63)")

        self.verticalLayout_2.addWidget(self.listWidget)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 65))
        self.frame_5.setStyleSheet(u"border: none;\n"
"background-color: rgb(43, 43, 43);\n"
"border-radius: 10px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(25)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.pushButton_2 = QPushButton(self.frame_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(25, 25))
        self.pushButton_2.setStyleSheet(u"opacity: 0;")
        icon3 = QIcon()
        icon3.addFile(u":/butt/C:/Users/ivans/Downloads/Group 1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(25, 25))
        self.pushButton.setStyleSheet(u"opacity: 0\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/butt/C:/Users/ivans/Downloads/Group 1 (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QSize(30, 30))
        self.pushButton.setAutoRepeatDelay(299)
        self.pushButton.setAutoRepeatInterval(103)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_5, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(30, 0))
        self.frame_3.setMaximumSize(QSize(20, 16777215))
        self.frame_3.setStyleSheet(u"border: none;\n"
"background-color: rgb(43, 43, 43);\n"
"border-radius: 10px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, -1, -1, -1)
        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(29, 0))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.pushButton_3 = QPushButton(self.frame_8)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(5, 100))
        self.pushButton_3.setMaximumSize(QSize(5, 16777215))
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"background-color: white;\n"
"border-radius: 2px\n"
"")

        self.horizontalLayout_4.addWidget(self.pushButton_3)


        self.verticalLayout_4.addWidget(self.frame_8, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.frame_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_4.setText("")
        self.pushButton_10.setText("")
        self.pushButton_9.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"previous song", None))
        self.pushButton_2.setText("")
        self.pushButton.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"next song", None))
        self.pushButton_3.setText("")
    # retranslateUi

