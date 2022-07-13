# Wmf

## Name
Weighted Median Filter

## Description
This repository contains all our work about optimizing weighted median filter during a one-month internship (June 2022) in the MICS laboratory.

## Last update
July 13, 2022

## Roadmap

Week 1 : 
 - Begin the bibliography
 - Collect img and build dataset
 - Try out the different filters that already exist

Week 2 :
 - Understand the 100x faster filtering from Zhang
 - Find metrics to evaluate the efficiency of filtering
 - Try to understand CUDA

Week 3 :
 - Chose the metrics
 - Finish the images generator to add noise over the different images
 
Week 4 :
 - Create a module for formatting the results
 - Close the project properly and document it
 
## Authors and acknowledgment
This project, initiated by Laurent Cabaret, is led by Tom Bray

## Project status
The internship is now over, you can contact Tom Bray at any time with questions: tom.bray@student-cs.fr

## Bibliography

Articles:
 - Brownrigg, D. R. K. « The Weighted Median Filter ». Communications of the ACM, vol. 27, nᵒ 8, août 1984, p. 807‑18. DOI.org (Crossref), https://doi.org/10.1145/358198.358222.
 
 - Lin Yin, et al. « Weighted median filters: a tutorial ». IEEE Transactions on Circuits and Systems II: Analog and Digital Signal Processing, vol. 43, nᵒ 3, mars 1996, p. 157‑92. DOI.org (Crossref), https://doi.org/10.1109/82.486465.

 - Zhang, Qi, et al. « 100+ Times Faster Weighted Median Filter (WMF) ». 2014 IEEE Conference on Computer Vision and Pattern Recognition, IEEE, 2014, p. 2830‑37. DOI.org (Crossref), https://doi.org/10.1109/CVPR.2014.362.

 - Zhao, Hanli, et al. « Real-Time Edge-Aware Weighted Median Filtering on the GPU ». Computers & Graphics, vol. 61, décembre 2016, p. 11‑18. DOI.org (Crossref), https://doi.org/10.1016/j.cag.2016.09.003.


Images:
 - http://www.cse.cuhk.edu.hk/~leojia/projects/L0smoothing/index.html#results
 - http://www.cse.cuhk.edu.hk/%7eleojia/projects/texturesep/tsmoothing.zip
 - https://mrl.cs.nyu.edu/projects/image-analogies/images/girl.jpg

## Python dependencies
You can install all the dependencies with:
    pip install -r src/python/requirements.txt

Here is the list of all python dependencies: 
 - numpy
 - matplotlib
 - opencv-contrib-python
 - sci-kit image

## Tips and ideas for the project
- In July 2022 nobody had yet parallelized Zhang's algorithm because the data structures are complicated to implement with parallel computing and call for previous calculations. However, there is something to dig into. 

- I didn't have time to make results on the efficiency of the filter according to the size of the kernel, it can be interesting!

- Do the weighted median filters keep the edges in place? We need to find measurements for this and do tests on the images.

- I found that for low noise levels, the filter tended to degrade the image more than to improve it but I didn't have time to find this noise threshold.