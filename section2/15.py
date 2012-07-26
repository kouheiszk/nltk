#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from nltk.book import *
from nltk.corpus import brown

brown_fileids = brown.fileids()
words = brown.words(fileids=brown_fileids)
fdist = nltk.FreqDist(words)
result = [w for w in fdist.keys() if fdist[w] >= 3]
