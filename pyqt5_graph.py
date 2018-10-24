# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/test2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import numpy as np
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui

from pylsl import StreamInlet, resolve_stream


class Ui_MainWindow(object):
    def __init__(self):
        self.streams = resolve_stream('type', 'EEG')
        self.inlet = StreamInlet(self.streams[0])

        self.is_start = True
        self.x = []
        self.y = []
        for i in range(16):
            self.y.append([])

        # self.x = 2*np.pi
        # self.time = list(np.linspace(0, self.x, 1000))

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
        self.StartButton.clicked.connect(self.start)

        self.StopButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.StopButton.setFont(font)
        self.StopButton.setObjectName("StopButton")
        self.horizontalLayout.addWidget(self.StopButton)
        self.StopButton.clicked.connect(self.stop)

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
        self.plot = self.guiplot.plot(pen="y")

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
        # tmpx = self.time[-1000:]
        # self.plot.setData(tmpx, np.sin(tmpx))
        # self.x += 2*np.pi*0.0001*10
        # self.time.append(self.x)

        if(self.is_start):
            sample, timestamp = self.inlet.pull_sample()
            for i in range(len(sample)):
                self.y[i].append(sample[i])
            self.x.append(timestamp)
            self.plot.setData(self.x[-1000:], self.y[0][-1000:])

    def start(self):
        self.is_start = True

    def stop(self):
        self.is_start = False
        data = [self.x]
        data.extend(self.y)
        df = pd.DataFrame(data).T
        df.to_excel("test.xlsx", index=False)


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
