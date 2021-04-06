from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Ввод имени', 'Enter your name:')

        if ok:
            with open('nickname.txt', 'w') as f:
                if text == "":
                    text = "PLAYER"
                f.write(text)