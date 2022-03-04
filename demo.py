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
from functions import *


# data
image1 = imread('data/image1.png')
image2 = imread('data/image2.png')
image3 = imread('data/image3.png')

images = np.dstack((image1, image2, image3))
# tree building
Bc = np.zeros((3, 3, 3), dtype=bool)
Bc[1, 1, :] = True
Bc[:, 1, 1] = True
Bc[1, :, 1] = True


#max tree
tree = siamxt.MaxTreeAlpha(images, Bc)
_ = duration_filter(tree, 1)
tempstabil = temp_stability_ratio(tree)


result = stability_filter(tree, 0.82)
show_images(result)

imsave("results/image1result.png", result[:, :, 0])
imsave("results/image2result.png", result[:, :, 1])
imsave("results/image3result.png", result[:, :, 2])
