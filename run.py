#!/usr/bin/env python
#
# Overall file to run full analysis pipeline given a set of raw corpus text
# files in UTF-8 format. Each text is also paired with a font appropriate for
# rendering that particular text using pangocairo.
#

from subprocess import call

## Sample Stage Constants
NUM_SAMPLES_FROM_RAW = 1000
SAMPLE_LENGTH_FROM_RAW = 8

## Render Stage Constants

rawTexts = [("bible-english-nt.txt", "Times New Roman"),
            ("bible-korean-nt.txt", "Times New Roman")]

for (fileName, font) in rawTexts:
    print "[Generate Samples][{}]".format(fileName)
    call(['./sampler.py', "rawCorpus/" + fileName, str(NUM_SAMPLES_FROM_RAW),
          str(SAMPLE_LENGTH_FROM_RAW), "corpus/" + "samp-" + fileName])



