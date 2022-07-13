import cv2 as cv
import noise
import numpy as np
import matplotlib.pyplot as plt


def similarity(img, filtered_img):

    height,width,x = np.shape(img)
    errorL2 = cv.norm( img, filtered_img, cv.NORM_L2 )

    similarity = 1-errorL2/(height * width)
    print(similarity)
    return similarity

img = cv.imread('img/9.jpg') 
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

noised = noise.noisy("s&p",img)

#Filter the image
blur = cv.ximgproc.weightedMedianFilter(noised,noised, 1, weightType = cv.ximgproc.WMF_COS)

#similarities
noised_sim = str(round(similarity(img,noised),3))
filtered_sim = str(round(similarity(img,blur),3))

#Display the original and the filtered image
plt.subplot(131),plt.imshow(noised),plt.title('Noised \n similarity = ' + noised_sim)
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(blur),plt.title('Filtered \n similarity = ' + filtered_sim)
plt.xticks([]), plt.yticks([])
plt.show()

