from re import S
import cv2 as cv
import numpy as np
import noise
from matplotlib import pyplot as plt


def similarity(img, filtered_img):

    height,width,x = np.shape(img)
    errorL2 = cv.norm( img, filtered_img, cv.NORM_L2 )

    similarity = 1-errorL2/(height * width)
    print(similarity)
    return similarity

img = cv.imread('img/9.jpg') 
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

noised = noise.noisy("s&p",img)

similarity(img, noised)