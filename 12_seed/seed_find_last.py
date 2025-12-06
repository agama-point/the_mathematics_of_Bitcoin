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
        print(num, "wodrs checkum-valid: ", word, keystore.bip39_is_checksum_valid(words))
        num += 1

"""
0 wodrs checkum-valid:  ability (True, True)
1 wodrs checkum-valid:  acoustic (True, True)
2 wodrs checkum-valid:  age (True, True)
3 wodrs checkum-valid:  alone (True, True)
4 wodrs checkum-valid:  anchor (True, True)
5 wodrs checkum-valid:  any (True, True)
...
125 wodrs checkum-valid:  win (True, True)
126 wodrs checkum-valid:  wise (True, True)
127 wodrs checkum-valid:  zone (True, True)
"""
