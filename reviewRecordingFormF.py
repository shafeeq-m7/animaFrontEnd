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
        MainWindow.setStyleSheet(u"background-color: #FCF4EB;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(75, 10, 591, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Helvetica Neue"])
        font.setPointSize(40)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"color: black")
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 10, 50, 50))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setBold(True)
        self.pushButton_4.setFont(font1)
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
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(740, 10, 50, 50))
        self.pushButton_3.setFont(font1)
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
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(670, 60, 58, 16))
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(160, 390, 191, 81))
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setPointSize(18)
        self.label_8.setFont(font3)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(750, 22, 30, 25))
        self.label_2.setStyleSheet(u"background-color: transparent;")
        self.label_2.setPixmap(QPixmap(u"../../Downloads/RemoveBG.png"))
        self.label_2.setScaledContents(True)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(150, 90, 571, 121))
        font4 = QFont()
        font4.setFamilies([u"Montserrat"])
        font4.setPointSize(22)
        font4.setBold(False)
        self.label_6.setFont(font4)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 60, 58, 16))
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(310, 190, 240, 60))
        self.label_13.setStyleSheet(u"background-color: transparent;")
        self.label_13.setPixmap(QPixmap(u"../../Downloads/Image with removed background.png"))
        self.label_13.setScaledContents(True)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 100, 58, 410))
        self.label_5.setStyleSheet(u"background-color: transparent;")
        self.label_5.setPixmap(QPixmap(u"../../Downloads/Removebg (1).png"))
        self.label_5.setScaledContents(True)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 20, 30, 30))
        self.label_4.setStyleSheet(u"background-color: transparent;")
        self.label_4.setPixmap(QPixmap(u"../../Downloads/Image with.png"))
        self.label_4.setScaledContents(True)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(740, 60, 58, 16))
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(670, 10, 50, 50))
        self.pushButton_2.setFont(font1)
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
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(200, 520, 111, 51))
        sizePolicy1.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy1)
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    background-color: #214EDF; /* Adjust the color to match your design */\n"
"    color: white;\n"
"    border-radius: 10px; /* Adjust the radius to match your design */\n"
"    font-family: 'Montserrat', sans-serif; /* Make sure Montserrat is installed */\n"
"    font-size: 18px; /* Adjust the size as needed */\n"
"    font-weight: bold;\n"
"    }\n"
"QPushButton:hover {\n"
"    background-color: #00de17; /* Lighter blue for hover effect */\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"../../Downloads/Image with (6).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QSize(30, 30))
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setFlat(True)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(460, 410, 261, 61))
        self.label_12.setFont(font3)
        self.label_12.setScaledContents(False)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_12.setWordWrap(True)
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(480, 520, 211, 51))
        sizePolicy1.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy1)
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"    background-color: #214EDF; /* Adjust the color to match your design */\n"
"    color: white;\n"
"    border-radius: 10px; /* Adjust the radius to match your design */\n"
"    font-family: 'Montserrat', sans-serif; /* Make sure Montserrat is installed */\n"
"    font-size: 18px; /* Adjust the size as needed */\n"
"    font-weight: bold;\n"
"    }\n"
"QPushButton:hover {\n"
"    background-color: #00de17; /* Lighter blue for hover effect */\n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../../Downloads/Image with (7).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QSize(30, 30))
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setFlat(True)
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(310, 270, 241, 51))
        sizePolicy1.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy1)
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"    background-color: #214EDF; /* Adjust the color to match your design */\n"
"    color: white;\n"
"    border-radius: 10px; /* Adjust the radius to match your design */\n"
"    font-family: 'Montserrat', sans-serif; /* Make sure Montserrat is installed */\n"
"    font-size: 18px; /* Adjust the size as needed */\n"
"    font-weight: bold;\n"
"    }\n"
"QPushButton:hover {\n"
"    background-color: #00de17; /* Lighter blue for hover effect */\n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../../Downloads/Image with (8).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon2)
        self.pushButton_7.setIconSize(QSize(30, 30))
        self.pushButton_7.setCheckable(False)
        self.pushButton_7.setFlat(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Review Recording", None))
        self.pushButton_4.setText("")
        self.pushButton_3.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"FAQs", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"If you're happy \n"
" with the recording: \n"
"\n"
" SELECT DONE", None))
        self.label_2.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"SELECT REVIEW RECORDING \n"
" To hear how you sound", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.label_13.setText("")
        self.label_5.setText("")
        self.label_4.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"DONE", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Otherwise, to record again: \n"
"\n"
" SELECT RECORD AGAIN", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"RECORD AGAIN", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"REVIEW RECORDING", None))
    # retranslateUi

