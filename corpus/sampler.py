#!/usr/bin/env python

import random
import sys

if len(sys.argv) != 4:
    print "usage: ./sampler.py <samplefile> <numsamples> <bytelength>"

SAMPLE_FILENAME = sys.argv[1]
NUM_SAMPLES = int(sys.argv[2])
SAMPLE_CAP = int(sys.argv[3])
SAMPLE_LENGTH = 8

numSamplesGenerated = 0

src = open(SAMPLE_FILENAME)
out = open("cut-" + SAMPLE_FILENAME, 'w')

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
    print(line)
    out.write(line.encode('utf-8') + '\n')
    numSamplesGenerated = numSamplesGenerated + 1

