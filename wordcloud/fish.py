#!/usr/bin/env python3

from PIL import Image
import numpy as np
from wordcloud import WordCloud

text = open('words.txt').read()

mask = np.array(Image.open('mask.png'))

wc = WordCloud(background_color=None, mask=mask, mode='RGBA', repeat=True, collocations=False, max_words=10000, regexp=r"[^\r\n]+")
wc.generate(text)
wc.to_file('fish.png')
