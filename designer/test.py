# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui


class CustomPlot(pg.GraphicsObject):
    def __init__(self, data):
        pg.GraphicsObject.__init__(self)
        self.data = data
        self.generatePicture()

    def generatePicture(self):
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w', width=1/2.))
        for (t, v) in self.data:
            p.drawLine(QtCore.QPointF(t, v-2), QtCore.QPointF(t, v+2))
        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # StartButton
        self.StartButtn = QtWidgets.QPushButton(self.centralwidget)
        self.StartButtn.setGeometry(QtCore.QRect(10, 10, 100, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.StartButtn.setFont(font)
        self.StartButtn.setObjectName("Start")
        self.StartButtn.clicked.connect(self.click1)

        # StopButton
        self.StopButton = QtWidgets.QPushButton(self.centralwidget)
        self.StopButton.setGeometry(QtCore.QRect(120, 10, 100, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.StopButton.setFont(font)
        self.StopButton.setObjectName("Stop")

        # SaveButton
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setGeometry(QtCore.QRect(230, 10, 100, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.SaveButton.setFont(font)
        self.SaveButton.setObjectName("Save")

        # Graph
        data = [
            (1., 10),
            (2., 13),
            (3., 17),
            (4., 14),
            (5., 13),
            (6., 15),
            (7., 11),
            (8., 16)
        ]
        MainWindow.addDockWidget(CustomPlot(data))

        # StatusBar
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.StartButtn.setText(_translate("MainWindow", "Start"))
        self.StopButton.setText(_translate("MainWindow", "Stop"))
        self.SaveButton.setText(_translate("MainWindow", "Save"))

    def click1(self):
        MainWindow.statusBar().showMessage('Push Button01')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
