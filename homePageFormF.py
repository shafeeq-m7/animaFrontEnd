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
        font = QFont()
        font.setFamilies([u"Trebuchet MS"])
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"background-color: #FCF4EB;\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 80, 175, 41))
        font1 = QFont()
        font1.setFamilies([u"Helvetica Neue"])
        font1.setPointSize(40)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"color: black")
        self.label.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(240, 460, 300, 61))
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setBold(True)
        self.pushButton.setFont(font2)
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
"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(290, 130, 225, 60))
        self.label_3.setPixmap(QPixmap(u"../../Desktop/Screenshot 2024-01-12 at 14.37.36.png"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(260, 220, 290, 154))
        self.label_4.setPixmap(QPixmap(u"../../Desktop/Screenshot 2024-01-12 at 14.57.41.png"))
        self.label_4.setScaledContents(True)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(210, 190, 441, 31))
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setPointSize(20)
        font3.setBold(False)
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color: black")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(120, 390, 581, 51))
        font4 = QFont()
        font4.setFamilies([u"Montserrat"])
        font4.setPointSize(18)
        font4.setBold(False)
        self.label_6.setFont(font4)
        self.label_6.setAcceptDrops(False)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setStyleSheet(u"color: black")
        self.label_6.setTextFormat(Qt.AutoText)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(710, 30, 50, 50))
        self.pushButton_2.setFont(font2)
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
"\n"
"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 20, 225, 60))
        self.label_2.setPixmap(QPixmap(u"../../Desktop/Screenshot 2024-01-12 at 14.37.28.png"))
        self.label_2.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Anima v3", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"START VOICE BANKING", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"The comprehensive voice banking solution", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Voice banking involves recording your own voice, this can then be used to create a digital voice that can read text for you", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.label_2.setText("")
    # retranslateUi

