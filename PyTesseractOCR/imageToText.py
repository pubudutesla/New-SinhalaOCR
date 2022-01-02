import xlsxwriter
import os
import re

import pytesseract as tess
from PIL import Image
tess.pytesseract.tesseract_cmd = r'C:\Users\Pubud\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

outWorkbook = xlsxwriter.Workbook("ocrData2.xlsx")
outSheet = outWorkbook.add_worksheet()



directory = os.fsencode('./rowAll')
i = 0
for file in os.listdir(directory):
     filename = os.fsdecode(file)
    #  if filename.endswith(".jpg"): 
    #  print('./row1/'+filename)
    #  print(filename)
    #  print(os.path.join(directory, filename))
    #  img =Image.open('./row1/data1.JPG')
     img =Image.open('./rowAll/'+filename)
     text = tess.image_to_string(img, lang='sin+eng')
    #  Replace new lines with a |
     mystring = text.replace('\n', ' | ').replace(' |  | ', '|').replace(' | ', '|')

    # split string by |
     array = mystring.split("|")
     x = 0
     y = 0
     z = 0
     for item in array:
    #    outSheet.write(x,0, item)
       #check if string has ascii
       checker = re.search(r"\[", item)
       print(item)
       if checker:
        #    print(checker)
           nonASCII = item.encode('ascii',errors='ignore')
           nonASCII_str = nonASCII.decode("utf-8")
           outSheet.write(x,0, nonASCII_str)
           x = x+1
    #    else:
    #         print('else'+ checker)
    #    elif len(item) == len(item.encode()) and len(item) >= 8:
    #        outSheet.write(y,1, item)
    #        y = y+1
    #    elif len(item) >= 8:
    #        outSheet.write(z,2, item)
    #        z = z+1
     i = i+1

outWorkbook.close()

#පි ගැ