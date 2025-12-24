#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This program converts a hexadecimal number ("ABC")
# first into decimal, then into binary.

h = "ABC"

# Convert hex → decimal
dec_value = int(h, 16)

# Convert decimal → binary (strip the "0b" prefix)
bin_value = bin(dec_value)[2:]

print("Hex:", h)
print("Dec:", dec_value)
print("Bin:", bin_value)

"""
Hex: ABC
Dec: 2748
Bin: 101010111100
"""