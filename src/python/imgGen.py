"""
This module is used to generate different images and test the filters and their effects. 
"""
import numpy as np
import matplotlib.pyplot as plt

def randImg(n, m, grayScale=False):
    """
    
    """
    if grayScale:
        return(np.random.rand(n,m))

    else:
        return(np.random.rand(n,m,3))

def uniformImg(n, m, color=[0.98,0,0]):
    """
    
    """
    return(np.full((n,m,3),color))

img = uniformImg(300,400)
print(img)
plt.imshow(img)
plt.show()