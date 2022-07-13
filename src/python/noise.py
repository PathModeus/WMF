'''
Parameters
----------
image : ndarray
    Input image data. Will be converted to float.
mode : str
    One of the following strings, selecting the type of noise to add:

    'gauss'  Gaussian-distributed additive noise.
    'poisson'   Poisson-distributed noise generated from the data.
    's&p'       Replaces random pixels with 0 or 1.
    'speckle'   Multiplicative noise using out = image + n*image,where
                n is uniform noise with specified mean & variance.
'''

import numpy as np
from skimage.util import random_noise

def noisy(noise_typ,image):

  #add gaussian noise
  if noise_typ == "gauss":
      
    noisy = random_noise(image, mode='gaussian')

  #add salt and pepper noise
  elif noise_typ == "s&p":

    amount = 0.05

    noisy = random_noise(image, mode='s&p',amount=amount)

  #add poisson noise  
  elif noise_typ == "poisson":

    noisy = random_noise(image, mode='poisson')

  #add speckle noise
  elif noise_typ =="speckle":
    
    mean = 0
    var = 0.01

    noisy = random_noise(mode = 'speckle', mean=mean, var=var)

  # The above function returns a floating-point image
  # on the range [0, 1], thus we changed it to 'uint8'
  # and from [0,255]
  noisy = np.array(255*noisy, dtype = 'uint8')

  return noisy