# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timeout.ui'
#
# Created: Mon Sep 15 15:38:32 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(396, 128)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.TimeDisplay = QtGui.QLCDNumber(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TimeDisplay.sizePolicy().hasHeightForWidth())
        self.TimeDisplay.setSizePolicy(sizePolicy)
        self.TimeDisplay.setNumDigits(8)
        self.TimeDisplay.setObjectName(_fromUtf8("TimeDisplay"))
        self.gridLayout.addWidget(self.TimeDisplay, 1, 0, 1, 1)
        self.hour1 = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hour1.sizePolicy().hasHeightForWidth())
        self.hour1.setSizePolicy(sizePolicy)
        self.hour1.setShortcut(_fromUtf8(""))
        self.hour1.setAutoDefault(True)
        self.hour1.setDefault(True)
        self.hour1.setObjectName(_fromUtf8("hour1"))
        self.gridLayout.addWidget(self.hour1, 1, 1, 1, 1)
        self.hour9 = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hour9.sizePolicy().hasHeightForWidth())
        self.hour9.setSizePolicy(sizePolicy)
        self.hour9.setShortcut(_fromUtf8(""))
        self.hour9.setAutoDefault(True)
        self.hour9.setDefault(True)
        self.hour9.setObjectName(_fromUtf8("hour9"))
        self.gridLayout.addWidget(self.hour9, 1, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">CAMERA DISCONNECTED!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">CLICK TO RECONNECT.</span></p></td></tr></table></body></html>", None))
        self.hour1.setText(_translate("Dialog", "One Hour\n"
"Extension", None))
        self.hour9.setText(_translate("Dialog", "Nine Hour\n"
"Extension", None))

