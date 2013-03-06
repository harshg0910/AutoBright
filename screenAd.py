# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screenAd.ui'
#
# Created: Wed Mar  6 01:28:28 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

#    Copyright (C) 2013
#    Pranav Gupta, Harsh Gupta, Anil Kag, Sparsh Sinha, Himanshu Bansal

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#---------------------------------------------------------------------

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Manual(object):
    def setupUi(self, Manual):
        Manual.setObjectName(_fromUtf8("Manual"))
        Manual.resize(364, 123)
        self.centralwidget = QtGui.QWidget(Manual)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalSlider = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(80, 30, 141, 19))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.spinBox = QtGui.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(30, 30, 42, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.ds = QtGui.QPushButton(self.centralwidget)
        self.ds.setGeometry(QtCore.QRect(230, 30, 41, 21))
        self.ds.setObjectName(_fromUtf8("ds"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 141, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 60, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        Manual.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Manual)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Manual.setStatusBar(self.statusbar)

        self.retranslateUi(Manual)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.spinBox.setValue)
        QtCore.QObject.connect(self.spinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.horizontalSlider.setValue)
        QtCore.QMetaObject.connectSlotsByName(Manual)

    def retranslateUi(self, Manual):
        Manual.setWindowTitle(QtGui.QApplication.translate("Manual", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.ds.setText(QtGui.QApplication.translate("Manual", "Set", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Manual", "Set Screen Brightness", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Manual", "Start", None, QtGui.QApplication.UnicodeUTF8))

