#-*-coding: utf-8 *-*
'''
Created on 21 mai 2012

@author: Askylh Snake
'''
from PyQt4.QtGui import QLCDNumber, QSlider, QWidget, QApplication
from PyQt4.QtCore import QObject, SIGNAL, SLOT, Qt, QCoreApplication
import os,sys
class MaFenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(200, 120)
        lcd = QLCDNumber(self)
        lcd.setSegmentStyle(QLCDNumber.Flat)
        lcd.move(60, 20)
        slider = QSlider(Qt.Horizontal, self)
        slider.setGeometry(10, 70, 150, 20)
        qApp = QCoreApplication.instance()
        self.connect(slider, SIGNAL("valueChanged(int)"), lcd, SLOT("display(int)"))
