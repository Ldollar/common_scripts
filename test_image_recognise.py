#!/user/bin/env python
# -*- coding:utf-8 -*-
import subprocess
import os
import Image
import ImageEnhance
from pytesseract import *
image = Image.open(r'E:\LOG\image\\frame\\all2\\timg.jpg')
print image
#使用ImageEnhance可以增强图片的识别率
enhancer = ImageEnhance.Contrast(image)
image_enhancer = enhancer.enhance(4)
#image.show()

# # Example config: '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
# # It's important to include double quotes around the dir path.
#tessdata_dir_config = '--tessdata-dir "C:\Program Files\Tesseract-OCR\\tessdata"'
# tessdata_dir_config = ‘--tessdata-dir "‘C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"‘
#pytesseract.image_to_string(image, config=tessdata_dir_config)
#pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

try:
    #tessdata_dir_config = '--tessdata-dir "C:\Program Files\Tesseract-OCR\\tessdata"'
    #tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    print pytesseract.image_to_string(image,lang='eng')
except Exception,e:
    print e