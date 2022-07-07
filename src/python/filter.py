"""
This function uses openCV to filter an img with a wmf, using Zhang, Qi, et al. algorithm
You can use weightType to modify the weight kernel of the filter. 
"""

import cv2 as cv
import noise
from matplotlib import pyplot as plt

#Load the image
img = cv.imread('img/9.jpg') 
img = cv.cvtColor(img, cv.COLOR_BGR2RGB) #by default OpenCV uses BGR rather than RGB

#Noised image
noised = noise.noisy("s&p",img)

#Filter the image
blur = cv.ximgproc.weightedMedianFilter(noised,noised, 1, weightType = cv.ximgproc.WMF_COS)

#Display the original and the filtered image
plt.subplot(121),plt.imshow(noised),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('MedianFilter')
plt.xticks([]), plt.yticks([])
plt.show()