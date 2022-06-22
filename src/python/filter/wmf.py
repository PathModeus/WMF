import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#Loading the image
img = cv.imread('img/basketball.png') 
img = cv.cvtColor(img, cv.COLOR_BGR2RGB) #by default OpenCV uses BGR rather than RGB

#Filtering the image
blur = cv.ximgproc.weightedMedianFilter(img,img, 1, weightType = cv.ximgproc.WMF_EXP)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('MedianFilter')
plt.xticks([]), plt.yticks([])
plt.show()