"""
Allows to present some results of my internship and calculations carried out according to various parameters.
"""
import cv2 as cv
import numpy as np
import noise
import matplotlib.pyplot as plt
import metrics as met
import imgGen

###Examples

images={}

clip_img = cv.imread('img/9.jpg')#load clipart image 
images['clip_img'] = { 'original' : cv.cvtColor(clip_img, cv.COLOR_BGR2RGB) }

standard_img = cv.imread('img/rock2.png')#load standard png image 
images['standard_img'] = { 'original' : cv.cvtColor(standard_img, cv.COLOR_BGR2RGB) }

uniform_img = imgGen.uniformImg(300, 400) #creates an uniform img
uniform_img = (255*uniform_img).astype(np.uint8)
images['uniform_img'] = { 'original' : uniform_img}

#gs_img = cv.imread('img/barbara.png')#load grayscale image 
#images['gs_img'] = { 'original' : cv.cvtColor(gs_img, cv.COLOR_BGR2RGB) }


#iterate over all the images
L=len(images)
i=0

for img in images : 
    #add noise over the images
    images[img]['noised'] = noise.noisy("s&p",images[img]['original'], 0.3)

    #filter the images
    images[img]['blured'] = cv.ximgproc.weightedMedianFilter(images[img]['noised'], images[img]['noised'], 3, weightType = cv.ximgproc.WMF_COS)

    #calculate similarities
    images[img]['noised_sim'] = str(round(met.similarity(images[img]['original'],images[img]['noised']),3))
    images[img]['blured_sim'] = str(round(met.similarity(images[img]['original'],images[img]['blured']),3))

    #Display the original, the noised and the filtered images
    plt.subplot(L*100+31+3*i),plt.imshow(images[img]['noised']),plt.title('Noised \n similarity = ' + images[img]['noised_sim'])
    plt.xticks([]), plt.yticks([])
    plt.subplot(L*100+32+3*i),plt.imshow(images[img]['original']),plt.title('Original \n similarity = 1')
    plt.xticks([]), plt.yticks([])
    plt.subplot(L*100+33+3*i),plt.imshow(images[img]['blured']),plt.title('Blured \n similarity = ' + images[img]['blured_sim'])
    plt.xticks([]), plt.yticks([])

    i+=1

plt.show()


###Quality of filter of a given kernel depending on noise lvl :

kernel_size=3
noiselvl = np.linspace(0,1,100)
quality = []

for i in noiselvl:
    quality.append(met.noiseDependentFilter(uniform_img, kernel_size, cv.ximgproc.WMF_COS, i))

plt.plot(noiselvl,quality)
plt.show()

###Quality of filter of the filter for a given noise lvl depending on kernel size :

kernel_size=[i for i in range(1, 26)]
noiselvl = 0.3
quality = []

for i in kernel_size:
    quality.append(met.noiseDependentFilter(uniform_img, i, cv.ximgproc.WMF_COS, noiselvl))

plt.plot(kernel_size,quality)
plt.show()