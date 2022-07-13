"""
This module is used to generate different images and test the filters and their effects. 
"""
import numpy as np
import matplotlib.pyplot as plt

def randImg(n, m, grayScale=False):
    """
    Generates an image composed entirely of random pixels.
    """
    if grayScale:
        return(np.random.rand(n,m))

    else:
        return(np.random.rand(n,m,3))

def uniformImg(n, m, color=[0.5,0.5,0.5]):
    """
    This function generates a uniform color image, the RGB colors are coded between 0 and 1.
    """
    return(np.full((n,m,3),color))

