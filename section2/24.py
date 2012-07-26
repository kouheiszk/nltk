#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
import random


# a

def top_of(cfd, num=50):
    return cfd.keys()[:num]


def random_choice(words):
    return random.choice(words)


text = nltk.corpus.genesis.words('english-kjv.txt')
bgrms = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bgrms)

words = top_of(cfd)
word = random_choice(words)
print word

# b

text = nltk.corpus.genesis.words('english-kjv.txt')
bgrms = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bgrms)
generate_model(cfd, random_choice(top_of(cfd)))

# c

text = nltk.corpus.genesis.words('english-kjv.txt')
bgrms1 = nltk.bigrams(text)

text = nltk.book.text1
bgrms2 = nltk.bigrams(text)

cfd = nltk.ConditionalFreqDist(bgrms1 + bgrms2)

generate_model(cfd, random_choice(top_of(cfd)))

