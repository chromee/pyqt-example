# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/16grid.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui

from pylsl import StreamInlet, resolve_stream


class Ui_MainWindow(object):
    def __init__(self):
        self.streams = resolve_stream('type', 'EEG')
        self.inlet = StreamInlet(self.streams[0])
        self.ch_count = self.inlet.info().channel_count()

        self.is_start = True
        self.x = []
        self.y = []
        for i in range(self.ch_count):
            self.y.append([])

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1083, 759)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1061, 731))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ButtonHorizontalLayout = QtWidgets.QHBoxLayout()
        self.ButtonHorizontalLayout.setObjectName("ButtonHorizontalLayout")
        self.StartButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.StartButton.setFont(font)
        self.StartButton.setObjectName("StartButton")
        self.ButtonHorizontalLayout.addWidget(self.StartButton)
        self.StopButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.StopButton.setFont(font)
        self.StopButton.setObjectName("StopButton")
        self.ButtonHorizontalLayout.addWidget(self.StopButton)
        self.SaveButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.SaveButton.setFont(font)
        self.SaveButton.setObjectName("SaveButton")
        self.ButtonHorizontalLayout.addWidget(self.SaveButton)
        self.verticalLayout.addLayout(self.ButtonHorizontalLayout)

        self.plots = []
        for i in range(self.ch_count):
            if (i % 4 == 0):
                horizontalLayout = QtWidgets.QHBoxLayout()
                self.verticalLayout.addLayout(horizontalLayout)
            graphicsObject = pg.PlotWidget()
            horizontalLayout.addWidget(graphicsObject)
            self.plots.append(graphicsObject.plot(pen="y"))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.StartButton.setText(_translate("MainWindow", "Start"))
        self.StopButton.setText(_translate("MainWindow", "Stop"))
        self.SaveButton.setText(_translate("MainWindow", "Save"))

    def update_plot(self):
        if(self.is_start):
            sample, timestamp = self.inlet.pull_sample()
            self.x.append(timestamp)
            for i in range(self.ch_count):
                self.y[i].append(sample[i])
                self.plots[i].setData(self.x[-1000:], self.y[i][-1000:])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    timer = QtCore.QTimer()
    timer.timeout.connect(ui.update_plot)
    timer.start(10)
    sys.exit(app.exec_())
