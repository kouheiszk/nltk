#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from nltk.book import *

def count_cmu(text):
    entries = nltk.corpus.cmudict.entries()
    word_cmu = {}
    for entry in entries:
        word, pron = entry
        word_cmu[word] = len(pron)
        
    count = 0
    for w in text:
        if word_cmu.has_key(w):
            count += word_cmu[w]
    
    return count


print count_cmu(['I', 'love', 'you', '.'])
print count_cmu(text1)