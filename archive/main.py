import sys
import random
import numpy as np
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5.QtGui import QIcon


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Button01", self)
        btn1.clicked.connect(self.Button01Clicked)

        self.statusBar()

        self.setWindowTitle('Button01')
        self.show()

    def Button01Clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' Push Button01')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("favicon.ico"))
    win = Window()
    sys.exit(app.exec_())
