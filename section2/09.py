#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from nltk.book import *

def get_unique_text(text):
    stopwords = nltk.corpus.stopwords.words("english")
    return sorted(set([w.lower() for w in text if w.isalpha() and w.lower() not in stopwords]))


uniq_text1 = get_unique_text(text1)
uniq_text2 = get_unique_text(text2)

common_words = [w for w in uniq_text1 if w in uniq_text2]
len(common_words)

text1.similar(common_words[0])
text2.similar(common_words[0])
