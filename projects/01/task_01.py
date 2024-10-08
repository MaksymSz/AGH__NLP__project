import os
from pathlib import Path
import pandas as pd
from collections import Counter

datapath = Path('../../data')

print(os.path.exists(datapath))

with open(datapath / 'corpus_raw.txt', 'r') as fh:
    corpus = fh.read()

corpus = corpus.split('\n')
corpus = filter(lambda s: not s.startswith('<'), corpus)
corpus = ' '.join(corpus)


