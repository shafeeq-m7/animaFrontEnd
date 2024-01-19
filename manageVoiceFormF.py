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
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(480, 300, 291, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setBold(True)
        self.pushButton_6.setFont(font)
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
"")
        icon = QIcon()
        icon.addFile(u"../../Downloads/Image with (13).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QSize(30, 30))
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setFlat(True)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(730, 10, 50, 50))
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
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(660, 10, 50, 50))
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
        self.label.setGeometry(QRect(70, 10, 581, 51))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Helvetica Neue"])
        font1.setPointSize(40)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"color: black")
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 150, 451, 31))
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setPointSize(30)
        font2.setBold(True)
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"color: black;")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 470, 58, 16))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 60, 58, 16))
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"color: black;")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(740, 22, 30, 25))
        self.label_2.setStyleSheet(u"background-color: transparent;")
        self.label_2.setPixmap(QPixmap(u"../../Downloads/RemoveBG.png"))
        self.label_2.setScaledContents(True)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 20, 30, 30))
        self.label_4.setStyleSheet(u"background-color: transparent;")
        self.label_4.setPixmap(QPixmap(u"../../Downloads/Image with.png"))
        self.label_4.setScaledContents(True)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(660, 60, 58, 16))
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"color: black;")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(480, 370, 291, 51))
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
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
        icon1.addFile(u"../../Downloads/Image with (14).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(30, 30))
        self.pushButton.setCheckable(False)
        self.pushButton.setFlat(True)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(480, 230, 291, 51))
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamilies([u"Montserrat"])
        font4.setBold(True)
        font4.setKerning(False)
        self.pushButton_5.setFont(font4)
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
        icon2 = QIcon()
        icon2.addFile(u"../../Downloads/Image with (12).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setIconSize(QSize(30, 30))
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setFlat(True)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(730, 60, 58, 16))
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"color: black;")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 10, 50, 50))
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
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
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 120, 451, 31))
        font5 = QFont()
        font5.setFamilies([u"Montserrat"])
        font5.setPointSize(22)
        font5.setBold(False)
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"color: black;")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(480, 440, 291, 51))
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
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
        icon3 = QIcon()
        icon3.addFile(u"../../Downloads/Image with removed background (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QSize(30, 30))
        self.pushButton_8.setCheckable(False)
        self.pushButton_8.setFlat(True)
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(20, 190, 441, 341))
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"    background-color: #214EDF; /* Adjust the color to match your design */\n"
"    color: white;\n"
"    border-radius: 5px; /* Adjust the radius to match your design */\n"
"    font-family: 'Montserrat', sans-serif; /* Make sure Montserrat is installed */\n"
"    font-size: 18px; /* Adjust the size as needed */\n"
"    font-weight: bold;\n"
"    }\n"
"\n"
"")
        self.pushButton_9.setIconSize(QSize(30, 30))
        self.pushButton_9.setCheckable(False)
        self.pushButton_9.setFlat(True)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(40, 200, 401, 31))
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"color: white;\n"
"background-color: transparent;")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(40, 280, 401, 31))
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"color: white;\n"
"background-color: transparent;")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(120, 240, 231, 31))
        self.label_7.setFont(font5)
        self.label_7.setStyleSheet(u"color: white;\n"
"background-color: transparent;")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(120, 330, 231, 31))
        self.label_8.setFont(font5)
        self.label_8.setStyleSheet(u"color: white;\n"
"background-color: transparent;")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(120, 360, 231, 31))
        self.label_15.setFont(font5)
        self.label_15.setStyleSheet(u"color: white;\n"
"background-color: transparent;")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(120, 390, 231, 31))
        self.label_16.setFont(font5)
        self.label_16.setStyleSheet(u"color: white;\n"
"background-color: transparent;")
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(120, 420, 231, 31))
        self.label_17.setFont(font5)
        self.label_17.setStyleSheet(u"color: white;\n"
"background-color: transparent;")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(380, 240, 31, 31))
        self.label_5.setStyleSheet(u"background-color: transparent;")
        self.label_5.setPixmap(QPixmap(u"../../Downloads/Image with (6).png"))
        self.label_5.setScaledContents(True)
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(380, 320, 31, 131))
        self.label_18.setStyleSheet(u"background-color: transparent;")
        self.label_18.setPixmap(QPixmap(u"../../Downloads/Image with (15).png"))
        self.label_18.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_4.raise_()
        self.pushButton_6.raise_()
        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.label.raise_()
        self.label_12.raise_()
        self.label_3.raise_()
        self.label_9.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_10.raise_()
        self.pushButton.raise_()
        self.pushButton_5.raise_()
        self.label_11.raise_()
        self.label_6.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_5.raise_()
        self.label_18.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"IMPORT VOICE", None))
        self.pushButton_3.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Manage Voices", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Enter Text:", None))
        self.label_3.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.label_2.setText("")
        self.label_4.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"FAQs", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"DELETE VOICE", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"REDO MY VOICE", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.pushButton_4.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Selected Voice: Sam", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"SELECT AS DEFAULT", None))
        self.pushButton_9.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Your Voice", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Other Voices", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Sam", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Tony Stark", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Peter Parker", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Jackie Chan", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Cristiano Ronaldo", None))
        self.label_5.setText("")
        self.label_18.setText("")
    # retranslateUi

