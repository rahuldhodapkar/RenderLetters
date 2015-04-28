#!/usr/bin/env python

import random
import sys
import progressbar

if len(sys.argv) != 5:
    print "usage: ./sampler.py <samplefile> <numsamples> <bytelength> <outfile>"

SAMPLE_FILENAME = sys.argv[1]
NUM_SAMPLES = int(sys.argv[2])
SAMPLE_LENGTH = int(sys.argv[3])
OUTFILE_NAME = sys.argv[4]
SAMPLE_CAP = 10000

numSamplesGenerated = 0

src = open(SAMPLE_FILENAME)
out = open(OUTFILE_NAME, 'w')

bar = progressbar.ProgressBar(maxval=NUM_SAMPLES, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', \
    progressbar.Percentage()]).start()

while numSamplesGenerated < NUM_SAMPLES:
    offset = random.randrange(SAMPLE_CAP)
    src.seek(offset)
    try:
        line = src.readline().decode('utf-8')
        line = line.strip()
    except:
        continue

    if (len(line) < SAMPLE_LENGTH):
        continue

    line = line[:SAMPLE_LENGTH]
    out.write(line.encode('utf-8') + '\n')
    numSamplesGenerated = numSamplesGenerated + 1
    bar.update(numSamplesGenerated)

bar.finish()

