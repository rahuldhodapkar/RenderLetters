#!/usr/bin/env python
#
# Overall file to run full analysis pipeline given a set of raw corpus text
# files in UTF-8 format. Each text is also paired with a font appropriate for
# rendering that particular text using pangocairo.
#

from subprocess import call

## Sample Stage Constants
NUM_SAMPLES_FROM_RAW = 10
SAMPLE_LENGTH_FROM_RAW = 8

## Render Stage Constants
RENDER_HEIGHT = 30
RENDER_WIDTH = 50

## PCA Stage Constants
NUM_PCA_COMPS = 5

rawTexts = [("bible-english-nt", "ENG" ,"Times New Roman 12"),
            ("bible-korean-nt", "KRN" ,"Times New Roman 10")]

for (fileNameRoot, prefix, fontStyleSize) in rawTexts:
    print "[Generate Samples][{}]".format(fileNameRoot)
    call(["./sampler.py",
        "rawCorpus/" + fileNameRoot + ".txt", str(NUM_SAMPLES_FROM_RAW),
        str(SAMPLE_LENGTH_FROM_RAW),
        "corpus/" + "samp-" + fileNameRoot + ".txt"])

    print "[Render Strings][{}]".format(fileNameRoot)
    call(["./builder.py", "corpus/" + "samp-" + fileNameRoot + ".txt",
          str(NUM_SAMPLES_FROM_RAW), prefix, fontStyleSize,
          str(RENDER_HEIGHT), str(RENDER_WIDTH), fileNameRoot])

    print "[Run PCA][{}]".format(fileNameRoot)
    call(["./pca.py", "processed/" + fileNameRoot,
          fileNameRoot, str(NUM_PCA_COMPS),
          str(RENDER_HEIGHT), str(RENDER_WIDTH)])




