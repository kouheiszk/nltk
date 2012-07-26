#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import swadesh

swadesh.fileids()
swadesh.words("en")
fr2en = swadesh.entries(["fr", "en"])
fr2en
translate = dict(fr2en)
translate["chien"]
translate["jeter"]
