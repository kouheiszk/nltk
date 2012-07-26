#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import brown
from nltk.corpus import webtext

brown.raw(fileids=["cm02"])
webtext.raw("firefox.txt")
