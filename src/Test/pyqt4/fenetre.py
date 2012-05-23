#-*-coding: utf-8 *-*
'''
Created on 21 mai 2012

@author: Askylh Snake
'''
from PyQt4.QtGui import QWidget, QPushButton, QFont , QIcon
from PyQt4.QtCore import Qt, QCoreApplication, SIGNAL, SLOT
import os,sys


class MaFenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(300, 150)
        # Construction du bouton
        m_bouton=QPushButton(QIcon("smil.png"), self.trUtf8("Pimp mon bouton !"), self)
        m_bouton.setFont(QFont("Comic Sans MS", 14))
        m_bouton.setCursor(Qt.ForbiddenCursor)
        #m_bouton.setIcon(QIcon("smil.png"))
        m_bouton.move(60, 50)
        qApp = QCoreApplication.instance()
        self.connect(m_bouton, SIGNAL("clicked()"), qApp, SLOT("quit()"))
        boutonAPropos=QPushButton(self.trUtf8("A propos"), self)
        boutonAPropos.setFont(QFont("Arial", 11))
        boutonAPropos.move(120, 90)
        #Connexion du clic du bouton à la fermeture de l'application
        self.connect(boutonAPropos, SIGNAL("clicked()"), qApp, SLOT("aboutQt()"));

