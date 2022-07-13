'''
Parameters
----------
image : ndarray
    Input image data. Will be converted to float.
mode : str
    One of the following strings, selecting the type of noise to add:

    'gauss'     Gaussian-distributed additive noise.
    'poisson'   Poisson-distributed noise generated from the data.
    's&p'       Replaces random pixels with 0 or 1.
    'speckle'   Multiplicative noise using out = image + n*image,where
                n is uniform noise with specified mean & variance.
'''

import numpy as np
import numpy as np
from skimage.util import random_noise

def noisy(noise_typ,image):

    if noise_typ == "gauss":

      V=0.05**2 #var

      noisy = random_noise(image, mode='gaussian', var=V)

    elif noise_typ == "s&p":
      
      a = 0.2 #amount of noise
      saltVsPepper = 0.5

      noisy = random_noise(image, mode='s&p', salt_vs_pepper=saltVsPepper, amount=a)


    elif noise_typ == "poisson":
      
      noisy = random_noise(image, mode='poisson')

    elif noise_typ =="speckle":
      M = 0 #Mean
      V = 0.05**2 #Var     
      noisy = random_noise(image, mode='speckle', mean=M, var=V)
    
    noisy = (255*noisy).astype(np.uint8)

    return noisy

