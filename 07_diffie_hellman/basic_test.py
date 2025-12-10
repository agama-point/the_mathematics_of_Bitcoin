#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crypto_agama.diffie_hellman import DiffieHellmanKeys

G = 2 # generator
p = 17
a = 5 # Alice: Private key

dh = DiffieHellmanKeys(G,p)
print(dh) # basic info

print("[ Parameters ]")
print("prime/modulo: ", dh.p)
print("---generator: ", dh.g)

print("[ --- Alice --- ]")
alice_private_key = a
alice_public_key = dh.generate_public_key(alice_private_key)
print("Public key:",alice_public_key)

"""
DiffieHellmanKeys
(g = 2, p = 17)

[ Parameters ]
prime/modulo:  17
---generator:  2
[ --- Alice --- ]
Public key: 15
"""