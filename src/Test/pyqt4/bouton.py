#­*­coding: utf­8 ­*­
'''
Created on 20 mai 2012

@author: Askylh Snake
'''
from PyQt4.QtGui import QApplication, QPushButton, QFont, QIcon, QWidget
from PyQt4 import QtCore

import sys


def main(args):
    app = QApplication(args)
    fenetre = QWidget()
    fenetre.setFixedSize(300, 150)
    bouton = QPushButton("hello world", fenetre)
    bouton.setText(app.trUtf8("hé des accents"))
    bouton.setToolTip(app.trUtf8("Ne sert à rien"))
    bouton.setFont(QFont("Comic Sans MS", 20, QFont.Bold, True))
    bouton.setCursor(QtCore.Qt.CrossCursor)
    bouton.setIcon(QIcon("smil.png"))
    bouton.setGeometry(60, 50, 280, 70)
    autreBouton=QPushButton(app.trUtf8("Et çui­ci ?"),bouton) #autre bouton fils du premier bouton
    autreBouton.setFont(QFont("Arial", 10,QFont.Bold,True))
    autreBouton.move(40,10)


    fenetre.show()
    r = app.exec_()
    return r

if __name__ == "__main__" :
    main(sys.argv)