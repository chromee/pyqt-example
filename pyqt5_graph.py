# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/test2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import numpy as np
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
        MainWindow.resize(814, 649)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)

        self.verticalLayoutWidget.setGeometry(QtCore.QRect(29, 19, 761, 601))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.StartButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.StartButton.setFont(font)
        self.StartButton.setObjectName("StartButton")
        self.horizontalLayout.addWidget(self.StartButton)

        self.StopButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.StopButton.setFont(font)
        self.StopButton.setObjectName("StopButton")
        self.horizontalLayout.addWidget(self.StopButton)

        self.SaveButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.SaveButton.setFont(font)
        self.SaveButton.setObjectName("SaveButton")
        self.horizontalLayout.addWidget(self.SaveButton)

        self.verticalLayout.addLayout(self.horizontalLayout)
        # self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        # self.widget.setObjectName("widget")
        # self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        # Graph
        self.guiplot = pg.PlotWidget()
        self.verticalLayout.addWidget(self.guiplot)
        self.y = self.guiplot.plot(pen="y")
        self.x = 2*np.pi
        self.time = list(np.linspace(0, self.x, 1000))

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def update_plot(self):
        self.y.setData(self.time, np.sin(self.time))
        self.x += 2*np.pi*0.0001*10
        self.time.append(self.x)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.StartButton.setText(_translate("MainWindow", "Start"))
        self.StopButton.setText(_translate("MainWindow", "Stop"))
        self.SaveButton.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    timer = QtCore.QTimer()
    timer.timeout.connect(ui.update_plot)
    timer.start(1)
    sys.exit(app.exec_())
