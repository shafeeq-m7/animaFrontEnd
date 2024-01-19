# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the homePageForm.py file
#     pyside6-uic form.ui -o homePageForm.py, or
#     pyside2-uic form.ui -o homePageForm.py
from homePageFormF import Ui_MainWindow as Ui_HomePage
from setUpPageFormF import Ui_MainWindow as Ui_SetUpPage
from setUpRecordingFormF import Ui_MainWindow as Ui_SetUpRecordingPage
from reviewRecordingFormF import Ui_MainWindow as Ui_ReviewRecordingPage
from existHomeFormF import Ui_MainWindow as Ui_ExistHomePage
from textToSpeechFormF import Ui_MainWindow as Ui_TextToSpeechPage
from manageVoiceFormF import Ui_MainWindow as Ui_ManageVoicePage

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_HomePage()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.openSetUpPage)

    def openSetUpPage(self):
        self.ui = Ui_SetUpPage()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.openHomePage) # back button goes to Home Page
        self.ui.pushButton_3.clicked.connect(self.openHomePage) # home button goes to Home Page
        self.ui.pushButton.clicked.connect(self.openSetUpRecordingPage) # START READING button goes to SetUpRecording Page


    def openHomePage(self):
        self.ui = Ui_HomePage()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.openSetUpPage)


    def openSetUpRecordingPage(self):
        self.ui = Ui_SetUpRecordingPage()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.openHomePage)
        self.ui.pushButton_4.clicked.connect(self.openSetUpPage)
        self.ui.pushButton_6.clicked.connect(self.openReviewRecordingPage)

    def openReviewRecordingPage(self):
        self.ui = Ui_ReviewRecordingPage()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.openHomePage)
        self.ui.pushButton_4.clicked.connect(self.openSetUpRecordingPage)
        self.ui.pushButton_6.clicked.connect(self.openSetUpRecordingPage)
        self.ui.pushButton_5.clicked.connect(self.openExistHomePage)

    def openExistHomePage(self):
        self.ui = Ui_ExistHomePage()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.openTextToSpeechPage)

    def openTextToSpeechPage(self):
        self.ui = Ui_TextToSpeechPage()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.openExistHomePage)
        self.ui.pushButton_3.clicked.connect(self.openExistHomePage)
        self.ui.pushButton.clicked.connect(self.openManageVoicePage)

    def openManageVoicePage(self):
        self.ui = Ui_ManageVoicePage()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.openTextToSpeechPage)
        self.ui.pushButton_3.clicked.connect(self.openExistHomePage)
        self.ui.pushButton_5.clicked.connect(self.openHomePage)










if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
