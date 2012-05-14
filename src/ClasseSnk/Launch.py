# -*- coding: utf-8 *-*
'''
Created on 8 mai 2012

@author: Askylh Snake
'''
#import Image
from OCRSnk import OCR
import pyscreenshot as IG


#img = Image.open('/home/chris/Documents/snake/Test/wina.bmp')
img=IG.grab(bbox=(0,0,185,20))

OCRimg = OCR(img, False, False )
print OCRimg.tostring()