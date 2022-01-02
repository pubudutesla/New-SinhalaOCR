
from PIL import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Pubud\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
import sys
from pdf2image import convert_from_path
import os
from datetime import datetime
import re

print("Started at ",datetime.now())

PDF_file = "./2017_Col_KadMC_12Mal_12A.pdf"
    
pages = convert_from_path(PDF_file, 500)
  
image_counter = 1
  
# Iterate through all the pages stored above
for page in pages:
  
    # Declaring filename for each page of PDF as JPG
    # For each page, filename will be:
    # PDF page n -> page_n.jpg
    filename = "page_"+str(image_counter)+".jpg"
      
    # Save the image of the page in system
    page.save(filename, 'JPEG')
  
    # Increment the counter to update filename
    image_counter = image_counter + 1

# filelimit = image_counter-1
  
# outfile = "out_text.txt"

# Line = namedtuple('Line', 'company_id company_name doctype open_amt_bc current months1 months2 months3')

# district_re = re.compile(r'පරිපාලන දිස්ත්‍රික්කය')
# line_re = re.compile(r'V\s+පි|V\s+ගැ')
# line_re = re.compile(r'\W(පි)')
  
# Open the file in append mode
# f = open(outfile, "a", encoding="utf-8")
  
# for i in range(1, filelimit + 1):
#     filename = "page_"+str(i)+".jpg"
#     img =Image.open(filename)
#     print(filename)
#     text = tess.image_to_string(img, lang='sin+eng')
#     # text = text.replace('-\n', '')    
#     # f.write(text)
#     match = line_re.search(text)
#     if match:
#         print(match)
#     else:
#         print('nope')
# f.close()

print("Ended at ",datetime.now())