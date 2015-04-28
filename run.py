#!/usr/bin/env python
#
# Overall file to run full analysis pipeline given a set of raw corpus text
# files in UTF-8 format. Each text is also paired with a font appropriate for
# rendering that particular text using pangocairo.
#

from subprocess import call

## Sample Stage Constants
NUM_SAMPLES_FROM_RAW = 100
SAMPLE_LENGTH_FROM_RAW = 8

## Render Stage Constants
RENDER_HEIGHT = 50
RENDER_WIDTH = 100

rawTexts = [("bible-english-nt", "ENG" ,"Times New Roman 30"),
            ("bible-korean-nt", "KRN" ,"Times New Roman 25")]

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

