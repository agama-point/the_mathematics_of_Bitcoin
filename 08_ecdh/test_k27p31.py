#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

# Add parent directory to import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crypto_agama.ecc import point_adding, point_doubling

print("--- Simple ECC Test ---")

# Elliptic curve parameters:
# Curve over F_p: y^2 = x^3 + a*x + b (mod p)
# Test curve used here: a = 0, b = 7, p = 17  →  y^2 = x^3 + 7 (mod 17)
a = 0
b = 7
p = 31

# Generator point G (example point on the curve)
Gx, Gy = 15, 13

print(f"Curve parameters: a={a}, b={b}, p={p}")
print(f"Generator G = ({Gx}, {Gy})")
print("\n--- Scalar multiplication by repeated adding ---")

# Print 1G explicitly
print(f"1 . ({Gx}, {Gy})")

# Start at G
dx, dy = Gx, Gy

# Compute 2G, 3G, ..., 17G
for gi in range(2, 31):
    if gi == 2:
        # The first step uses doubling: 2G = G + G
        dx, dy = point_doubling(dx, dy, a=a, p=p)
    else:
        # General case: (n+1)G = G + nG
        dx, dy = point_adding(Gx, Gy, dx, dy, p=p)

    print(f"{gi} . ({dx}, {dy})")

print("=" * 40)
print("k27 [11011] = k1+k2 + k8+k16")
print("Verification test:")

# Precomputed points from the loop (for p=17 curve)
k1 = (15, 13)
k2 = (29, 17)
k8 = (11,27)
k16 = (3,13)

# Point addition test: 8G + 2G should equal 10G
r1 = point_adding(k1[0], k1[1], k2[0], k2[1], p=p)
print("Result1: 1G + 2G =", r1)
r2 = point_adding(k8[0], k8[1], k16[0], k16[1], p=p)
print("Result2: 8G + 16G =", r2)
r3 = point_adding(r1[0], r1[1], r2[0], r2[1], p=p)
print("Result3: 3G + 24G =", r3)

"""
--- Simple ECC Test ---
Curve parameters: a=0, b=7, p=31
Generator G = (15, 13)

--- Scalar multiplication by repeated adding ---
1 . (15, 13) *
2 . (29, 17) *
3 . (1, 22)
4 . (20, 19)
5 . (21, 17)
6 . (23, 23)
7 . (12, 14)
8 . (11, 27) **
9 . (25, 22)
10 . (7, 19)
11 . (27, 27)
12 . (5, 9)
13 . (0, 24)
14 . (4, 12)
15 . (22, 23)
16 . (3, 13) **
17 . (13, 18)
18 . (17, 23)
19 . (24, 4)
20 . (24, 27)
21 . (17, 8)
22 . (13, 13)
23 . (3, 18)
24 . (22, 8)
25 . (4, 19)
26 . (0, 7)
27 . (5, 22) ***
28 . (27, 4)
29 . (7, 12)
30 . (25, 9)
========================================
k27 [11011] = k1+k2 + k8+k16
Verification test:
Result1: 1G + 2G = (1, 22)
Result2: 8G + 16G = (22, 8)
Result3: 3G + 24G = (5, 22)
"""