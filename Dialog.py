import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.uic import loadUi
from Cleaner import Cleaner

class MainPage(QDialog):
    def __init__(self):
        super(MainPage,self).__init__()
        loadUi('Homepage.ui', self)
        self.pushButton.clicked.connect(self.get_text)
        self.setWindowTitle("Reddit Cleaner")
        self.textEdit.setReadOnly(True)


    def get_text(self):
        words = self.plainTextEdit.toPlainText()
        cleaner = Cleaner()
        words2 = cleaner.edit_bulk_comments(words)

        for item in words2:
            self.textEdit.append(item)


app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec())