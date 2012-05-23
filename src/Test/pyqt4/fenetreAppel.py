#-*-coding: utf-8 *-*
'''
Created on 21 mai 2012

@author: Askylh Snake
'''
import fenetre , sys
from PyQt4.QtGui import QApplication

def main(args):
    app = QApplication(args)
    lfenetre=fenetre.MaFenetre()
    lfenetre.show()
    r = app.exec_()
    return r 

if __name__=="__main__":
    main(sys.argv)