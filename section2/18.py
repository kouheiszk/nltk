#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk

brown_fileids = nltk.corpus.brown.fileids()

sents = nltk.corpus.brown.sents(fileids=brown_fileids)
stopwords = set(nltk.corpus.stopwords.words("english"))
results = []

for sent in sents:
    bigrams = nltk.bigrams(sent)
    for bigram in bigrams:
        word1, word2 = bigram
        if word1.lower() not in stopwords and word2.lower() not in stopwords and word1.isalnum() and word2.isalnum():
            results.append((word1.lower(), word2.lower()))

fdist = FreqDist(results)
fdist.keys()[:50]
