#!/usr/bin/env python

import random
import sys
import progressbar
from subprocess import call

if len(sys.argv) != 7:
    print "usage: ./builder.py <samplefile> " + \
          "<image_prefix> <font_size_and_style> " + \
          "<image_height> <image_width> <outfile_folder>"

SAMPLE_FILENAME = sys.argv[1]
SAMPLE_PREFIX = sys.argv[2]
FONT_STYLE_AND_SIZE = sys.argv[3]

RENDER_HEIGHT = int(sys.argv[4])
RENDER_WIDTH = int(sys.argv[5])

OUTFILE_FOLDERNAME = sys.argv[6]

i = 1
with open(...) as f:
    for line in f:
        call(["mkdir", "/processed/{}/".format(OUTFILE_FOLDERNAME)])
        call(["render/render", str(RENDER_WIDTH), str(RENDER_HEIGHT),
              FONT_STYLE_AND_SIZE, line,
              "/processed/{}/{}.png".format(OUTFILE_FOLDERNAME, str(i))])
        i = i + 1


