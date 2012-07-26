#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from nltk.book import *

def vacab_size(text):
    return len(set([w.lower() for w in text if w.isalnum()]))

vacab_size(text5)
