import datetime
from os.path import exists

from WorkToRest import Ui_Dialog
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *


class window(QtWidgets.QDialog):
    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.text_trt = ''
        self.text_twt = ''

        self.timer_twt = QtCore.QTimer(self)
        self.timer_twt.timeout.connect(self.run_watch_twt)
        self.timer_twt.setInterval(1)

        self.timer_trt = QtCore.QTimer(self)
        self.timer_trt.timeout.connect(self.run_watch_trt)
        self.timer_trt.setInterval(1)

        self.mscounter_twt = 0
        self.mscounter_trt = 0
        self.isreset_twt = True
        self.isreset_trt = True

        self.ui.start_twt.clicked.connect(self.startTwt)
        self.ui.stop_twt.clicked.connect(self.stopTwt)
        self.ui.start_trt.clicked.connect(self.startTrt)
        self.ui.stop_trt.clicked.connect(self.stopTrt)
        self.ui.savedata.clicked.connect(self.savedata)
        self.ui.show_graph.clicked.connect(self.show_graphs)

        self.stopwatch_twt()
        self.stopwatch_trt()


    def run_watch_twt(self):
        self.ui.savedata.setDisabled(False)
        self.mscounter_twt = self.mscounter_twt + 1
        self.stopwatch_twt()

    def run_watch_trt(self):
        self.ui.savedata.setDisabled(False)
        self.mscounter_trt = self.mscounter_trt + 1
        self.stopwatch_trt()

    def stopwatch_twt(self):
        self.text_twt = str(datetime.timedelta(milliseconds=self.mscounter_twt))[:-7]
        self.ui.lcdNumber_twt.setDigitCount(9)
        if not self.isreset_twt:
            self.ui.lcdNumber_twt.display(self.text_twt)
        else:
            self.ui.lcdNumber_twt.display('0:00:00')

    def startTwt(self):
        self.timer_twt.start()
        self.timer_trt.stop()
        self.isreset_twt = False
        self.ui.start_twt.setDisabled(True)
        self.ui.stop_twt.setDisabled(False)
        self.ui.stop_trt.setDisabled(True)

    def stopTwt(self):
        self.timer_twt.stop()
        self.ui.start_twt.setDisabled(False)
        self.ui.stop_twt.setDisabled(True)

    def stopwatch_trt(self):
        self.text_trt = str(datetime.timedelta(milliseconds=self.mscounter_trt))[:-7]
        self.ui.lcdNumber_trt.setDigitCount(9)
        if not self.isreset_trt:
            self.ui.lcdNumber_trt.display(self.text_trt)
        else:
            self.ui.lcdNumber_trt.display('0:00:00')

    def startTrt(self):
        self.timer_trt.start()
        self.timer_twt.stop()
        self.isreset_trt = False
        self.ui.stop_twt.setDisabled(True)
        self.ui.start_twt.setDisabled(False)
        self.ui.stop_trt.setDisabled(False)

    def stopTrt(self):
        self.timer_trt.stop()
        self.ui.stop_trt.setDisabled(True)

    def savedata(self):
        if self.text_trt == '' and self.text_twt == '':
            return
        self.timer_twt.stop()
        self.timer_trt.stop()
        self.mscounter_trt = 0
        self.mscounter_twt = 0
        self.ui.lcdNumber_trt.display('0:00:00')
        self.ui.lcdNumber_twt.display('0:00:00')
        self.ui.savedata.setDisabled(True)
        self.ui.stop_trt.setDisabled(True)
        if exists('data.oil'):
            with open('data.oil', 'a') as f:
                if self.text_trt == '':
                    f.write(str(datetime.date.today()) + "\n" + self.text_twt +  "\n" +  '0:00:00' + "\n\n")
                elif self.text_twt == '':
                    f.write(str(datetime.date.today()) + "\n" + '0:00:00' + "\n" + self.text_trt + "\n\n")
                else:
                    f.write(str(datetime.date.today()) + "\n" + self.text_twt + "\n" + self.text_trt + "\n\n")
        else:
            with open('data.oil', 'w') as f:
                f.write('\n')
                if self.text_trt == '':
                    f.write(str(datetime.date.today()) + "\n" + self.text_twt +  "\n" +  '0:00:00' + "\n\n")
                elif self.text_twt == '':
                    f.write(str(datetime.date.today()) + "\n" + '0:00:00' + "\n" + self.text_trt + "\n\n")
                else:
                    f.write(str(datetime.date.today()) + "\n" + self.text_twt + "\n" + self.text_trt + "\n\n")

        self.text_trt = ''
        self.text_twt = ''

    def show_graphs(self):
        from plots import main_graph




app = QApplication([])
apps = window()
apps.show()

app.exec()