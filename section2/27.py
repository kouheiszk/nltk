#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import nltk
from nltk.corpus import wordnet as wn

samples = ['n', 'v', 'a', 'r']

for sample in samples:
    total = 0
    words = set()
    for synset in wn.all_synsets(sample):
        for w in synset.lemma_names:
            if w not in words:
                words.add(w)
                total += len(wn.synsets(w, sample))

    print "%s : %f" %(sample, total / len(words))