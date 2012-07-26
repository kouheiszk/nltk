#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk

entries = nltk.corpus.cmudict.entries()

prev = ''
words = []
common = []

for entry in entries:
    word, pron = entry
    if word == prev:
        common.append(word)
        entry
    words.append(word)
    prev = word

print len(words) - len(set(words))
print len(common)
