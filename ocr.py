import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import timeit
import pytesseract
%matplotlib inline

filenames = os.listdir('G:/New dataset/Tesseract/Images')
print(filenames)

img = cv2.imread("G:/New dataset/Tesseract/images/plate1.png") # image in BGR format
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)  # binary thresholding
## this function shows two images side-by-side
# this function will plot two images side by side
def plot_two_images(img1, img2, title1="", title2=""):
    fig = plt.figure(figsize=[15,15])
    ax1= fig.add_subplot(121)
    ax1.imshow(img1, cmap="gray")
    ax1.set(xticks=[], yticks=[], title=title1)
    
    ax2= fig.add_subplot(122)
    ax2.imshow(img2, cmap="gray")
    ax2.set(xticks=[], yticks=[], title=title2)
plot_two_images(img, thresh3, 'Original image', 'Processed image')

text = pytesseract.image_to_string(thresh3, lang='ben' )
print(text)