# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setToolTipDuration(0)
        MainWindow.setStyleSheet(u"background-color: #FCF4EB;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(670, 10, 50, 50))
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #214EDF; /* Replace with the color of your choice */\n"
"    color: white;\n"
"    border-radius: 25px; /* Adjust for a circular shape */\n"
"    font-size: 16px; /* Adjust as needed */\n"
"    font-weight: bold;\n"
"    min-width: 50px; /* Adjust to ensure the button is round */\n"
"    max-width: 50px; /* Adjust to ensure the button is round */\n"
"    min-height: 50px; /* Adjust to ensure the button is round */\n"
"    max-height: 50px; /* Adjust to ensure the button is round */\n"
"    icon-size: 40px 40px; /* Adjust based on your icon size */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #00de17; /* Lighter blue for hover effect */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1c54b2; /* Darker blue for pressed effect */\n"
"}\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(195, 10, 411, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Helvetica Neue"])
        font1.setPointSize(40)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"color: black")
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(260, 500, 251, 61))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #214EDF; /* Adjust the color to match your design */\n"
"    color: white;\n"
"    border-radius: 10px; /* Adjust the radius to match your design */\n"
"    font-family: 'Montserrat', sans-serif; /* Make sure Montserrat is installed */\n"
"    font-size: 18px; /* Adjust the size as needed */\n"
"    font-weight: bold;\n"
"    padding: 10px 20px; /* Adjust padding to match your design */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #00de17; /* Lighter blue for hover effect */\n"
"}\n"
"\n"
"")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(740, 10, 50, 50))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"    background-color: #214EDF; /* Replace with the color of your choice */\n"
"    color: white;\n"
"    border-radius: 25px; /* Adjust for a circular shape */\n"
"    font-size: 16px; /* Adjust as needed */\n"
"    font-weight: bold;\n"
"    min-width: 50px; /* Adjust to ensure the button is round */\n"
"    max-width: 50px; /* Adjust to ensure the button is round */\n"
"    min-height: 50px; /* Adjust to ensure the button is round */\n"
"    max-height: 50px; /* Adjust to ensure the button is round */\n"
"    icon-size: 40px 40px; /* Adjust based on your icon size */\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #00de17; /* Lighter blue for hover effect */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1c54b2; /* Darker blue for pressed effect */\n"
"}\n"
"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(750, 22, 30, 25))
        self.label_2.setStyleSheet(u"background-color: transparent;")
        self.label_2.setPixmap(QPixmap(u"../../Downloads/RemoveBG.png"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(465, 517, 31, 25))
        self.label_3.setStyleSheet(u"background-color: transparent;")
        self.label_3.setPixmap(QPixmap(u"../../Downloads/Removebg Preview Jan 14 Screenshot.png"))
        self.label_3.setScaledContents(True)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 10, 50, 50))
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"    background-color: #214EDF; /* Replace with the color of your choice */\n"
"    color: white;\n"
"    border-radius: 25px; /* Adjust for a circular shape */\n"
"    font-size: 16px; /* Adjust as needed */\n"
"    font-weight: bold;\n"
"    min-width: 50px; /* Adjust to ensure the button is round */\n"
"    max-width: 50px; /* Adjust to ensure the button is round */\n"
"    min-height: 50px; /* Adjust to ensure the button is round */\n"
"    max-height: 50px; /* Adjust to ensure the button is round */\n"
"    icon-size: 40px 40px; /* Adjust based on your icon size */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #00de17; /* Lighter blue for hover effect */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1c54b2; /* Darker blue for pressed effect */\n"
"}\n"
"")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 20, 30, 30))
        self.label_4.setStyleSheet(u"background-color: transparent;")
        self.label_4.setPixmap(QPixmap(u"../../Downloads/Image with.png"))
        self.label_4.setScaledContents(True)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 100, 58, 410))
        self.label_5.setPixmap(QPixmap(u"../../Desktop/Screenshot 2024-01-14 at 16.52.18.png"))
        self.label_5.setScaledContents(True)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(190, 80, 401, 121))
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setPointSize(22)
        font2.setBold(False)
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(600, 90, 75, 100))
        self.label_7.setPixmap(QPixmap(u"../../Downloads/Image with (1).png"))
        self.label_7.setScaledContents(True)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(140, 240, 541, 231))
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setPointSize(18)
        self.label_8.setFont(font3)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 60, 58, 16))
        font4 = QFont()
        font4.setFamilies([u"Montserrat"])
        font4.setPointSize(16)
        font4.setBold(True)
        self.label_9.setFont(font4)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(670, 60, 58, 16))
        self.label_10.setFont(font4)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(740, 60, 58, 16))
        self.label_11.setFont(font4)
        self.label_11.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label.raise_()
        self.pushButton_3.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButton_4.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Voice Set Up", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"START READING", None))
        self.pushButton_3.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.pushButton_4.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Select START READING \n"
"\n"
"Next, begin reading the text below", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Jack, a quick-witted explorer, found himself venturing beyond the azure mountains. As he zigzagged through the verdant forest, he stumbled upon a mysterious alcove. Unfazed, he decoded the cryptic glyphs, revealing the forgotten lore of an ancient civilisation. Hypnotised by the harmonious cadence of a distant waterfall, he mused, 'The quest for wisdom is the quintessence of life.' Shortly afterwards, he recited the numbers one to ten, capturing the essence of his vocal range.", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"FAQs", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
    # retranslateUi

