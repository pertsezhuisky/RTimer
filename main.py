#################################
#     Project: RTimer           #
#     Author: Roman Kizhaev      #
#     Github: pertsezhuisky     #
#################################

import datetime
from os.path import exists
from WorkToRest import UiDialog
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *


class window(QtWidgets.QDialog):
    def __init__(self):
        """ initial setup """
        super(window, self).__init__()
        self.ui = UiDialog()
        self.ui.setupUi(self)
        # define timer objects and other variables
        self.text_trt = ''
        self.text_twt = ''
        self.timer_twt = QtCore.QTimer(self)
        self.timer_twt.timeout.connect(self.run_watch_twt)
        self.timer_twt.setInterval(1)
        self.timer_trt = QtCore.QTimer(self)
        self.timer_trt.timeout.connect(self.run_watch_trt)
        self.timer_trt.setInterval(1)
        # main counters of time
        self.mscounter_twt = 0
        self.mscounter_trt = 0
        # define status of stop button
        self.isreset_twt = True
        self.isreset_trt = True
        # define button clicks and connecting them with modules
        self.ui.start_twt.clicked.connect(self.startTwt)
        self.ui.stop_twt.clicked.connect(self.stopTwt)
        self.ui.start_trt.clicked.connect(self.startTrt)
        self.ui.stop_trt.clicked.connect(self.stopTrt)
        self.ui.savedata.clicked.connect(self.savedata)
        self.ui.show_graph.clicked.connect(self.show_plots)
        # launching main functions
        self.stopwatch_twt()
        self.stopwatch_trt()

    # Modules' block for first LCDNumber object lcdNumber_twt (TWT - Total Working Time) #
    def run_watch_twt(self):
        """ setting up the timer """
        self.ui.savedata.setDisabled(False)
        self.mscounter_twt = self.mscounter_twt + 1  # making counter for our timer
        self.stopwatch_twt()

    def stopwatch_twt(self):
        """ calculation difference between counter and now time """
        # main calculations. You be able to edit format of time by changing
        self.text_twt = str(datetime.timedelta(milliseconds=self.mscounter_twt))[:-7]
        self.ui.lcdNumber_twt.setDigitCount(9)
        if not self.isreset_twt:  # checking if stop button isn't clicked
            self.ui.lcdNumber_twt.display(self.text_twt)
        else:
            self.ui.lcdNumber_twt.display('0:00:00')

    def startTwt(self):
        """ launch main process for TWT timer """
        self.timer_twt.start()  # start working of timer_twt
        self.timer_trt.stop()  # stop working of timer_trt if it was launched before
        self.isreset_twt = False  # flag that launch displaying data to LCDNumber
        self.ui.start_twt.setDisabled(True)
        self.ui.stop_twt.setDisabled(False)
        self.ui.stop_trt.setDisabled(True)

    def stopTwt(self):
        """ stop the timer not reload it """
        self.timer_twt.stop()
        self.ui.start_twt.setDisabled(False)
        self.ui.stop_twt.setDisabled(True)

    # Modules' block for second LCDNumber object lcdNumber_trt (TrT - Total Rest Time) #
    def run_watch_trt(self):
        """ setting up the timer """
        self.ui.savedata.setDisabled(False)
        self.mscounter_trt = self.mscounter_trt + 1
        self.stopwatch_trt()

    def stopwatch_trt(self):
        """ calculation difference between counter and now time """
        self.text_trt = str(datetime.timedelta(milliseconds=self.mscounter_trt))[:-7]
        self.ui.lcdNumber_trt.setDigitCount(9)
        if not self.isreset_trt:
            self.ui.lcdNumber_trt.display(self.text_trt)
        else:
            self.ui.lcdNumber_trt.display('0:00:00')

    def startTrt(self):
        """ launch main process for TRT timer """
        self.timer_trt.start()
        self.timer_twt.stop()
        self.isreset_trt = False
        self.ui.stop_twt.setDisabled(True)
        self.ui.start_twt.setDisabled(False)
        self.ui.stop_trt.setDisabled(False)

    def stopTrt(self):
        """ stop the timer not reload it """
        self.timer_trt.stop()
        self.ui.stop_trt.setDisabled(True)

    def savedata(self):
        """ saving data and check status of file """
        # if user didn't launch both - timer's program won't record data
        if self.text_trt == '' and self.text_twt == '':
            return
        # stop all timers
        self.timer_twt.stop()
        self.timer_trt.stop()
        # reloading counters to zero
        self.mscounter_trt = 0
        self.mscounter_twt = 0
        self.ui.lcdNumber_trt.display('0:00:00')
        self.ui.lcdNumber_twt.display('0:00:00')
        self.ui.savedata.setDisabled(True)
        self.ui.stop_trt.setDisabled(True)
        if exists('data.oil'):  # if file have already created
            with open('data.oil', 'a') as f:  # edit file and recording data
                if self.text_trt == '':  # if text_trt have no data then we print 0:00:00
                    f.write(str(datetime.date.today()) + "\n" + self.text_twt + "\n" + '0:00:00' + "\n\n")
                elif self.text_twt == '':
                    f.write(str(datetime.date.today()) + "\n" + '0:00:00' + "\n" + self.text_trt + "\n\n")
                else:  # print all data
                    f.write(str(datetime.date.today()) + "\n" + self.text_twt + "\n" + self.text_trt + "\n\n")
        else:  # if file doesn't exist
            with open('data.oil', 'w') as f:  # creating file
                f.write('\n')  # if you delete the "\n" you will kill whole program
                if self.text_trt == '':
                    f.write(str(datetime.date.today()) + "\n" + self.text_twt + "\n" + '0:00:00' + "\n\n")
                elif self.text_twt == '':
                    f.write(str(datetime.date.today()) + "\n" + '0:00:00' + "\n" + self.text_trt + "\n\n")
                else:
                    f.write(str(datetime.date.today()) + "\n" + self.text_twt + "\n" + self.text_trt + "\n\n")
        # note about "\n": we need to create "\n\n" for indicating the new block of data.

        # reload variables
        self.text_trt = ''
        self.text_twt = ''

    def show_plots(self):
        """ making and showing plots """
        from plots import main_graph
        main_graph()


app = QApplication([])
apps = window()
apps.show()

app.exec()
