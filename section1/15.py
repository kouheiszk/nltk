#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from nltk.book import *

for b in sorted([w for w in set(text5) if w.startswith("b")]):
    print b
