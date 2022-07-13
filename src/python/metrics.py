"""
This module contains all the metrics and measurements to evaluate the qualities of the different filters according to the parameters.
"""
import numpy as np
import cv2 as cv
import noise


def similarity(img, filtered_img):
    """
    This function calculates the similarity between two images, typically the original one and another one that has been filtered.
    """

    height,width,x = np.shape(img)
    errorL2 = cv.norm( img, filtered_img, cv.NORM_L2 )

    similarity = 1-errorL2/(height * width)

    return similarity

def qualityMeasurement(sim_filtered, sim_noised):
    """
    Calculates the quality of the filter.
    If the ratio is greater than 1 the filter has improved the quality of the image compared to the noisy image.
    If it is less than 1 the quality is degraded. 
    This measure is not very formalized.
    """

    return(sim_filtered/sim_noised)

def noiseDependentFilter(img, kern_size, kern_type, noiseLvl):
    """
    Calculates the quality of the filter for a given noise level and the dimensions and type of a given kernel
    kern_type : https://docs.opencv.org/3.4/d9/d29/namespacecv_1_1ximgproc.html#ae01330ec6648a4971b7aa3076b595cd6
     - cv.ximgproc.WMF_EXP
     - cv.ximgproc.WMF_IV1 
     - cv.ximgproc.WMF_IV2 
     - cv.ximgproc.WMF_COS 
     - cv.ximgproc.WMF_JAC 
     - cv.ximgproc.WMF_OFF
    """

    #add noise over the image
    noised = noise.noisy("s&p",img, noiseLvl)

    #filter the image
    blur = cv.ximgproc.weightedMedianFilter(noised,noised, kern_size, weightType = kern_type)

    #calculates similarities
    noised_sim = similarity(img, noised)
    filtered_sim = similarity (img, blur)

    #calculates the quality
    qual = qualityMeasurement(filtered_sim, noised_sim)

    return qual
