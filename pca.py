#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python script to analyze the results of an arbitrary character set
# generation. Runs PCA algorithm from sklearn package.

import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob

from subprocess import call
import sys

if len(sys.argv) != 6:
    print "usage: ./pca.py <image_folder_path> <nameRoot> <num_pca_comps>" + \
          " <img_height> <img_width>"

IMAGE_FOLDER_PATH = sys.argv[1]
NAME_ROOT = sys.argv[2]
NUM_PCA_COMPS = int(sys.argv[3])

IMG_HEIGHT = int(sys.argv[4])
IMG_WIDTH = int(sys.argv[5])

path = IMAGE_FOLDER_PATH + "/*.png"
files = glob.glob(path)

i = 0
dataPoints = []
for name in files:
    img = mpimg.imread(name)
    img = img[:, :, 0]
    img = np.reshape(img, (-1, 1))
    img = np.asarray(img)[:,0]
    dataPoints.append(img)
    i = i + 1

X = np.array(dataPoints)

pca = PCA(n_components=NUM_PCA_COMPS)
pca.fit(X)

call(["mkdir", "results/{}".format(NAME_ROOT)])
call(["mkdir", "results/{}/data".format(NAME_ROOT)])

dataOut = open("results/{}/data/summary.csv".format(NAME_ROOT), "w")

for i in range(0, NUM_PCA_COMPS):
    print >>dataOut, "{}, {}, {}".format(i, pca.components_[i],
            pca.explained_variance_ratio_[i])

#print pca.components_
#print pca.explained_variance_ratio_

call(["mkdir", "results/{}/eigs".format(NAME_ROOT)])

for i in range(0, len(pca.components_)):
    v = np.array(pca.components_[i])
    v = np.reshape(v, (IMG_HEIGHT, IMG_WIDTH) )
    mpimg.imsave("results/{}/eigs/eig_{}.png".format(NAME_ROOT, i), v)

