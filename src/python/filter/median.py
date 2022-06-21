import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#Loading the image
img = cv.imread('img/basketball.png') 
img = cv.cvtColor(img, cv.COLOR_BGR2RGB) #by default OpenCV uses BGR rather than RGB

#Filtering the image
blur = cv.medianBlur(img,27)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()