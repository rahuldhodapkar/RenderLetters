#!/usr/bin/env python
#
# Python script to generate graphs of the "y-axis" variance of the images
# from the generated corpus set.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob

import progressbar

import sys
from subprocess import call

import warnings
warnings.simplefilter("always")

if len(sys.argv) != 5:
    print "usage: ./yvar.py <image_folder_path> <nameRoot>" + \
          " <img_height> <img_width>"

IMAGE_FOLDER_PATH = sys.argv[1]
NAME_ROOT = sys.argv[2]

IMG_HEIGHT = int(sys.argv[3])
IMG_WIDTH = int(sys.argv[4])

path = IMAGE_FOLDER_PATH + "/*.png"

print "[YVAR][{}][Parsing Image Folder]".format(NAME_ROOT)
files = glob.glob(path)

print "[YVAR][{}][Loading Image Files]".format(NAME_ROOT)
bar = progressbar.ProgressBar(maxval=len(files), \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', \
    progressbar.Percentage()]).start()

i = 0
combinedSamples = []
for name in files:
    img = mpimg.imread(name)
    img = img[:, :, 0]
    vects = np.vsplit(img, IMG_HEIGHT)

    j = 0
    for vect in vects:
        if len(combinedSamples) <= j:
            combinedSamples.append(vect)
        else:
            combinedSamples[j] = np.append(combinedSamples[j], vect, axis=0)
        j = j + 1

    i = i + 1
    bar.update(i)
bar.finish()

varVals = []
for sampSet in combinedSamples:
    meanVect = np.mean(sampSet, axis=0)
    varVect = np.var(sampSet, axis=0)
    varVals.append(np.sum(varVect))

call(["mkdir", "results/{}".format(NAME_ROOT)])
call(["mkdir", "results/{}/yvar".format(NAME_ROOT)])
call(["mkdir", "results/{}/yvar/figs".format(NAME_ROOT)])

plt.plot(varVals)
plt.savefig("results/{}/yvar/figs/{}-yvarplot.png".format(NAME_ROOT, NAME_ROOT))

