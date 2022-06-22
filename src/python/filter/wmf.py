"""
This function uses openCV to filter an img with a wmf, using Zhang, Qi, et al. algorithm
You can use weightType to modify the weight kernel of the filter. 
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#Load the image
img = cv.imread('img/basketball.png') 
img = cv.cvtColor(img, cv.COLOR_BGR2RGB) #by default OpenCV uses BGR rather than RGB

#Filter the image
blur = cv.ximgproc.weightedMedianFilter(img,img, 1, weightType = cv.ximgproc.WMF_EXP)

#Display the original and the filtered image
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('MedianFilter')
plt.xticks([]), plt.yticks([])
plt.show()