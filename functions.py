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

def show_images(a):
    b=a.shape[2]
    for i in range(b):
       plt.figure()
       plt.imshow(a[:,:,i], cmap='gray',vmin=0,vmax=255)
       plt.show()
def temp_stability_ratio(tree):
    #with some existed nodes
    nodesize=tree.node_array.shape[1]

    r,c,b=tree.shape
    area=np.zeros([nodesize,b])
    tempstability=np.zeros(nodesize)
    for i in range(nodesize):
        a=tree.recConnectedComponent(i,bbonly = False)
        for j in range(b):
            area[i,j]=np.count_nonzero(a[:,:,j])
    for i in range(nodesize):
        for j in range(b-1):
            if area[i,j+1]==0 or area[i,j]==0:
                c=0
            else:
                c=min(area[i,j],area[i,j+1])/max(area[i,j],area[i,j+1])
            tempstability[i]+=c

    tempstability=tempstability/(b-1)
    return tempstability
def stability_filter(tree, t):
    stability = temp_stability_ratio(tree)
    node = np.where(stability < t)
    nodes = np.ones(tree.node_array.shape[1])
    nodes[node] = False
    nodes = np.array(nodes, dtype=bool)
    tree.prune(nodes)
    result = tree.getImage()
    return result
def border(im):
    im = 255 - im
    im[0, :, :] = 0
    im[:, 0, :] = 0
    im[:, -1, :] = 0
    im[-1, :, :] = 0
    return im
    

