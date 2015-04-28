#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python script to analyze the results of an arbitrary character set
# generation. Runs PCA algorithm from sklearn package.

import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob

print "testing inclusions"

#img = mpimg.imread('letterSet/፣.png')
path = 'letterSet/*.png'
files = glob.glob(path)


#limit = 50
i = 0

dataPoints = []
for name in files:
    print name
    img = mpimg.imread(name)

    print "original size was {} by {}".format(len(img), len(img[0]))
    img = img[:, :, 0]
    img = np.reshape(img, (-1, 1))
    #img = np.squeeze(np.asarray(img))
    print "original size was {}".format(len(img))
    img = np.asarray(img)[:,0]

    dataPoints.append(img)

    i = i + 1
    print "on {} of {}".format(i, len(files))
#    if i >= limit:
#        break

X = np.array(dataPoints)

print X

pca = PCA(n_components=5)
pca.fit(X)

print pca.components_
print pca.explained_variance_ratio_

for i in range(0, len(pca.components_)):
    v = np.array(pca.components_[i])
    v = np.reshape(v, (np.sqrt(len(v)),np.sqrt(len(v))) )
    mpimg.imsave("primaryComponents/eig_{}.png".format(i), v)

