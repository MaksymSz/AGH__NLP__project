import utils
import random
from itertools import compress
from pprint import pprint

skeleton = {
    "D_0": ...,
    "Adj_0": ...,
    "N_0": ...,
    "Adv": ...,
    "V": ...,
    "D_1": ...,
    "Adj_1": ...,
    "N_1": ...,
    "TENSE": ...
}

TENSES = (3, 4, 5)


def build_sentence(r):
    optionals = random.choices((False, True), k=5)
    optionals.insert(2, True)
    optionals.insert(4, True)
    optionals.append(True)
    tense = random.choices(TENSES)[0]
    r = list(r)
    r[4] = (r[4][tense],)
    r = compress(r, optionals)
    sentence = ' '.join([x[0] for x in r])
    sentence = sentence.capitalize()
    return sentence


def random_sentence(n_sentences=10):
    for r in utils.get_words(limit=n_sentences):
        yield build_sentence(r)


pprint(list(random_sentence()))
