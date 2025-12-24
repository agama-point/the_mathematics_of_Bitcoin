#!/usr/bin/env python
# -*- coding: utf-8 -*-
# agama_point: find last word from seed (around 128 validated)

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crypto_agama.agama_seed_tools import seed_words
from cryptos import * # pip install wheel, pbkdf2, cryptos
# from priv_data import get_words # words

bip39 = seed_words()

words_test11 = "major easy ignore body rule stay gorilla eager arch actor scan "

print("-"*30)

num = 0
for word in bip39:
    words = words_test11 + word
   
    if (keystore.bip39_is_checksum_valid(words)[0]):
        print(num, "words checkum-valid: ", word, keystore.bip39_is_checksum_valid(words))
        num += 1

"""
0 words checkum-valid:  ability (True, True)
1 words checkum-valid:  acoustic (True, True)
2 words checkum-valid:  age (True, True)
3 words checkum-valid:  alone (True, True)
4 words checkum-valid:  anchor (True, True)
5 words checkum-valid:  any (True, True)
6 words checkum-valid:  army (True, True)
7 words checkum-valid:  auction (True, True)
8 words checkum-valid:  awkward (True, True)
...
125 words checkum-valid:  win (True, True)
126 words checkum-valid:  wise (True, True)
127 words checkum-valid:  zone (True, True)
"""
