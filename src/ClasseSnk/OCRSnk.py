# -*- coding: utf-8 *-*
'''
Created on 8 mai 2012

@author: Askylh Snake

Inspired by Chris John Riley [PoC] tesseract OCR script -
    tuned for scr.im captcha :blog.c22.cc
'''


import Image
import ImageOps
from tesseract import image_to_string


class OCR(object):
    "Classe OCR permet d'extraire le texte d'une image"
    def __init__(self, image, invert=False, bold=False):
        self.img = image
        self.invert = invert
        self.bold = bold

    def invertVid(self):
        "video inverse noir devient blanc et blanc devient noir"
        self.img = ImageOps.invert(self.img)

    def tobold(self):
        "Augmente le contraste en remplaçant les valeurs moyennes grise en noir "
        self.pixdata = self.img.load()  # permet de lire les infos des pixels, dépend du mode de l'image
        for self.y in xrange(self.img.size[1]):
            for self.x in xrange(self.img.size[0]):
                if self.pixdata[self.x, self.y] < 150:
                    self.pixdata[self.x, self.y] = 0

    def tostring(self):
        #2 fois plus grand en bicubique (il me semble que cela donne de meilleur résultat)
        self.img = self.img.resize((self.img.size[0] * 2,
        self.img.size[1] * 2), Image.BICUBIC)
        # convertit en noir et blanc (niveaux de gris)
        self.img = self.img.convert("L")
        if self.invert:
            self.invertVid()
        if self.bold:
            self.tobold()
        self.img = self.img.resize((self.img.size[0] * 2,
        self.img.size[1] * 2), Image.NEAREST)
        return image_to_string(self.img)

if __name__ == "__main__":

    img = Image.open('/home/chris/Documents/snake/Test/wina.bmp')
    OCRimg = OCR(img, False, True)
    print(OCR(img, False, True).tostring())
