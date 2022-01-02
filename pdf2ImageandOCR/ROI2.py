import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Pubud\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from cv2 import cv2
from PIL import Image
import matplotlib.pyplot as plt

im = cv2.imread('page_1.jpg')

#-----------
def show_images(titles, images):
    # titles = ['dilate']
    # images = [dilate]
    _range = len(images)

    for i in range(_range):
        plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])

    plt.show()
#-----------

gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (9,9), 0)
# thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,30)
thresh2 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Dilate to combine adjacent text contours
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
dilate = cv2.dilate(thresh2, kernel, iterations=4)

# Invert image and perform morphological operations
# inverted = 255 - thresh2
# kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
# close = cv2.morphologyEx(thresh2, cv2.MORPH_CLOSE, kernel2, iterations=1)


# Find contours and filter using aspect ratio and area
cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    area = cv2.contourArea(c)
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.01 * peri, True)
    x,y,w,h = cv2.boundingRect(approx)
    aspect_ratio = w / float(h)
    if (aspect_ratio >= 2.5 or area < 75):
        fin_im = cv2.drawContours(dilate, [c], -1, (255,255,255), -1)
        
titles = ['fin_im', 'fin_im']
images = [fin_im, fin_im]
show_images(titles, images)

# line_items_coordinates = []
# for c in cnts:
#     area = cv2.contourArea(c)
#     x,y,w,h = cv2.boundingRect(c)

#     if y >= 100 and x <= 2500:
#         if area > 10000:
#             image = cv2.rectangle(im, (x,y), (4000, y+h), color=(255,0,255), thickness=3)
#             line_items_coordinates.append([(x,y), (2200, y+h)])

#     if y >= 2400 and x<= 2000:
#         image = cv2.rectangle(im, (x,y), (4000, y+h), color=(255,0,255), thickness=3)
#         line_items_coordinates.append([(x,y), (4000, y+h)])
    
# cv2.imwrite(r'xregionified3.jpg',image)

# Blur and perform text extraction
# thresh = cv2.GaussianBlur(thresh, (3,3), 0)
# data = tess.image_to_string(thresh, lang='sin+eng',config='--psm 6')
# print(data)

# cv2.imshow('close', close)
# cv2.imshow('thresh', thresh)
# cv2.waitKey()

#--------------------------------------------------------------------------------------
# # Dilate to combine adjacent text contours
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
# dilate = cv2.dilate(thresh, kernel, iterations=12)

# # Find contours, highlight text areas, and extract ROIs
# cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# # print(cnts)
# cnts = cnts[0] if len(cnts) == 2 else cnts[1]

# line_items_coordinates = []
# for c in cnts:
#     area = cv2.contourArea(c)
#     x,y,w,h = cv2.boundingRect(c)

#     if y >= 100 and x <= 2500:
#         if area > 10000:
#             image = cv2.rectangle(im, (x,y), (4000, y+h), color=(255,0,255), thickness=3)
#             line_items_coordinates.append([(x,y), (2200, y+h)])

#     if y >= 2400 and x<= 2000:
#         image = cv2.rectangle(im, (x,y), (4000, y+h), color=(255,0,255), thickness=3)
#         line_items_coordinates.append([(x,y), (4000, y+h)])
    
# cv2.imwrite(r'xregionified3.jpg',image)

#############################################################################################################
#@@@@@@@@@ OCR Part
# # load the original image
# image = cv2.imread('page_1.jpg')

# for i in range(1, 10 + 1):
#     # get co-ordinates to crop the image
#     c = line_items_coordinates[i]

#     # cropping image img = image[y0:y1, x0:x1]
#     img = image[c[0][1]:c[1][1], c[0][0]:c[1][0]]    

#     # convert the image to black and white for better OCR
#     ret,thresh1 = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
    
#     # img show #
#     titles = ['thresh1']
#     images = [thresh1]
#     for i in range(1):
#         plt.subplot(1, 1, i+1), plt.imshow(images[i], 'gray')
#         plt.title(titles[i])
#         plt.xticks([]),plt.yticks([])

#     plt.show()
#     # /img show #

#     # pytesseract image to string to get results
#     text = str(tess.image_to_string(thresh1, lang='sin+eng', config='--psm 6'))
#     print(text)