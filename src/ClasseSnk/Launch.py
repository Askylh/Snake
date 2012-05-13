# -*- coding: utf-8 *-*
'''
Created on 8 mai 2012

@author: Askylh Snake
'''
#import Image
from OCRSnk import OCR
import pyscreenshot as IG


#img = Image.open('/home/chris/Documents/snake/Test/wina.bmp')
img=IG.grab(bbox=(400,80,815,97))

OCRimg = OCR(img, True, True)
print OCRimg.tostring()