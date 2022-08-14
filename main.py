import datetime

from WorkToRest import Ui_Dialog

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *


class window(QtWidgets.QDialog):
    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

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
        self.timer_twt.stop()
        self.timer_trt.stop()
        self.mscounter_trt = 0
        self.mscounter_twt = 0
        self.ui.lcdNumber_trt.display('0:00:00')
        self.ui.lcdNumber_twt.display('0:00:00')
        self.ui.stop_trt.setDisabled(True)
        try:
            with open('data.txt', 'a') as f:
                f.write(str(datetime.date.today()) + "\n" + self.text_twt +  "\n" +  self.text_trt + "\n\n")
        except FileNotFoundError:
            with open('data.txt', 'w') as f:
                f.write(str(datetime.date.today()) + "\n" + self.text_twt +  "\n" +  self.text_trt + "\n\n")

    def show_graphs(self):
        import matplotlib as mpl
        import matplotlib.pyplot as plt
        import numpy as np
        import datetime

        import matplotlib.dates

        from datetime import datetime

        x_values = [datetime(2021, 11, 18, 12), datetime(2021, 11, 18, 14), datetime(2021, 11, 18, 16)]
        y_values = [1.0, 3.0, 2.0]

        dates = matplotlib.dates.date2num(x_values)
        matplotlib.pyplot.plot_date(dates, y_values)

        def data_to_lists():
            with open("data.txt", "r") as f:
                flag_1 = False
                flag_2 = False
                flag_3 = False
                flag_date = False
                date = []
                time_twt = []
                time_trt = []
                f_list = list(f)
                for i in range(len(f_list)):
                    new_list = f_list[i].split("\n")
                    if flag_1 == True and flag_date == False:
                        date.append(new_list[0])
                        flag_date = True
                    if new_list[0] == "":
                        flag_1 = True
                    if i == 2 or (i + 4) % 2 == 0 and new_list[0] != "":
                        flag_2 = True
                        time_twt.append(new_list[0])
                    if flag_1 == True and flag_2 == True and i != 2 and (i + 4) % 2:
                        flag_3 = True
                        time_trt.append(new_list[0])
                    if flag_3 == True:
                        flag_1 = False
                        flag_2 = False
                        flag_3 = False
                        flag_date = False

                f.close()
                list_to_digits(date, time_twt, time_trt)

        def list_to_digits(date, time_twt, time_trt):
            v = str
            print(date)
            print(time_twt)
            print(time_trt)
            dict = {}
            for i in range(len(date)):
                print(dict)

            data_to_lists()





app = QApplication([])
apps = window()
apps.show()

app.exec()