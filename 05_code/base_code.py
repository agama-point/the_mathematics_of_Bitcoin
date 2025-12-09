#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crypto_agama.agama_transform_tools import hex_to_bin, num_to_bin, num_to_hex, num_to_bech

print("simple example | bin | hex | bech32")
print("-"*30)
for i in range(16):
    print(f"{i} | {num_to_bin(i,6)} | {num_to_hex(i)} | {num_to_bech(i)}")