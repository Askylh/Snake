
#-*-coding: utf-8 *-*
'''
Created on 19 mai 2012

@author: Askylh Snake
'''
from Pyside.QtGui import QApplication
import os, sys


def main(args):
    a=Qapplication(args)
    r=a.exec_()
    return r

if __name__=="__main__" :
    main(sys.argv)