from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui


class UiDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(532, 321)
        Dialog.setAcceptDrops(False)
        Dialog.setSizeGripEnabled(False)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 50, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(280, 50, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(40, 90, 461, 51))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lcdNumber_twt = QtWidgets.QLCDNumber(self.widget)
        self.lcdNumber_twt.setObjectName("lcdNumber_twt")
        self.horizontalLayout.addWidget(self.lcdNumber_twt)
        self.lcdNumber_trt = QtWidgets.QLCDNumber(self.widget)
        self.lcdNumber_trt.setObjectName("lcdNumber_trt")
        self.horizontalLayout.addWidget(self.lcdNumber_trt)
        self.savedata = QtWidgets.QPushButton(Dialog)
        self.savedata.setGeometry(QtCore.QRect(230, 210, 75, 23))
        self.savedata.setObjectName("savedata")
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(40, 150, 77, 54))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.start_twt = QtWidgets.QPushButton(self.widget1)
        self.start_twt.setObjectName("start_twt")
        self.verticalLayout_2.addWidget(self.start_twt)
        self.stop_twt = QtWidgets.QPushButton(self.widget1)
        self.stop_twt.setObjectName("stop_twt")
        self.verticalLayout_2.addWidget(self.stop_twt)
        self.widget2 = QtWidgets.QWidget(Dialog)
        self.widget2.setGeometry(QtCore.QRect(420, 150, 77, 54))
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.start_trt = QtWidgets.QPushButton(self.widget2)
        self.start_trt.setObjectName("start_trt")
        self.verticalLayout.addWidget(self.start_trt)
        self.stop_trt = QtWidgets.QPushButton(self.widget2)
        self.stop_trt.setObjectName("stop_trt")
        self.show_graph = QtWidgets.QPushButton(Dialog)
        self.show_graph.setObjectName("show_graph")
        self.show_graph.setGeometry(QtCore.QRect(222, 235, 91, 23))
        self.verticalLayout.addWidget(self.stop_trt)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "RTimer"))
        self.label.setText(_translate("Dialog", "Total working time"))
        self.label_2.setText(_translate("Dialog", "Total rest time"))
        self.savedata.setText(_translate("Dialog", "Save data"))
        self.show_graph.setText(_translate("Dialog", "Show Plots"))
        self.start_twt.setText(_translate("Dialog", "Start"))
        self.stop_twt.setText(_translate("Dialog", "Stop"))
        self.start_trt.setText(_translate("Dialog", "Start"))
        self.stop_trt.setText(_translate("Dialog", "Stop"))


if __name__ == "__main__":
    app = QApplication([])
    apl = QtWidgets.QMainWindow()
    ui = UiDialog()
    ui.setupUi(apl)
    apl.show()
    app.exec()
