import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np

app = QtGui.QApplication([])

win = pg.GraphicsWindow(title="Basic plotting examples")
win.resize(1000, 600)
win.setWindowTitle('pyqtgraph example: Plotting')

interval = 0.0001  # milisec

plot = win.addPlot(title="Updating plot")
y = plot.plot(pen='y')
x = 2*np.pi
time = list(np.linspace(0, x, 1000))


def update():
    global y, time, x, interval
    y.setData(time, np.sin(time))
    x += 2*np.pi*interval*10
    time.append(x)


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(interval*1000)

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
