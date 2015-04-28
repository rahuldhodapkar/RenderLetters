#!/usr/bin/env python

import random
import sys
import progressbar
from subprocess import call

if len(sys.argv) != 8:
    print "usage: ./builder.py <samplefile> <numsamples> " + \
          "<image_prefix> <font_size_and_style> " + \
          "<image_height> <image_width> <outfile_folder>"

SAMPLE_FILENAME = sys.argv[1]
NUM_SAMPLES = int(sys.argv[2])
SAMPLE_PREFIX = sys.argv[3]
FONT_STYLE_AND_SIZE = sys.argv[4]

RENDER_HEIGHT = int(sys.argv[5])
RENDER_WIDTH = int(sys.argv[6])

OUTFILE_FOLDERNAME = sys.argv[7]

bar = progressbar.ProgressBar(maxval=NUM_SAMPLES, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', \
    progressbar.Percentage()]).start()

i = 0
with open(SAMPLE_FILENAME, 'r') as f:
    call(["mkdir", "processed/{}/".format(OUTFILE_FOLDERNAME)])
    for line in f:
        call(["render/render", str(RENDER_WIDTH), str(RENDER_HEIGHT),
              FONT_STYLE_AND_SIZE, line,
              "processed/{}/{}.png".format(OUTFILE_FOLDERNAME, str(i + 1))])
        i = i + 1
        bar.update(i)

bar.finish()

