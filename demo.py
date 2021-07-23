#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 14:19:08 2019

@author: caglayantuna
"""

import siamxt
from scipy import stats
from imageio import imread, imsave
import numpy as np
import matplotlib.pyplot as plt


# data
image1 = imread('data/image1.png')
image2 = imread('data/image2.png')
image3 = imread('data/image3.png')

images = np.dstack((image1, image2, image3))
# tree building
Bc = np.zeros((3,3,3), dtype = bool)
Bc[1, 1, :] = True
Bc[:, 1, 1] = True
Bc[1, :, 1] = True


#min tree
tree1 = siamxt.MaxTreeAlpha(images, Bc)
#duration_filter(tree1,1)
tempstabil=temp_stability_ratio(tree1)

#nodes=np.where(tempstabil<1.7)[0]
#result=sum_of_nodes(tree1,nodes)
result=stability_filter(tree1,0.1)
show_images(result)

show_images(border(images))