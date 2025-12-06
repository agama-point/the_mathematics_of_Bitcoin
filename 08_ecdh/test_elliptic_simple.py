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
p = 17

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
for gi in range(2, 18):
    if gi == 2:
        # The first step uses doubling: 2G = G + G
        dx, dy = point_doubling(dx, dy, a=a, p=p)
    else:
        # General case: (n+1)G = G + nG
        dx, dy = point_adding(Gx, Gy, dx, dy, p=p)

    print(f"{gi} . ({dx}, {dy})")

print("=" * 40)
print("Verification test: 8G + 2G = 10G")

# Precomputed points from the loop (for p=17 curve)
P8 = (1, 12)
P2 = (2, 10)

# Point addition test: 8G + 2G should equal 10G
result = point_adding(P8[0], P8[1], P2[0], P2[1], p=p)
print("8G + 2G =", result)

"""
--- Simple ECC Test ---
Curve parameters: a=0, b=7, p=17
Generator G = (15, 13)

--- Scalar multiplication by repeated adding ---
1 . (15, 13)
2 . (2, 10)
3 . (8, 3)
4 . (12, 1)
5 . (6, 6)
6 . (5, 8)
7 . (10, 15)
8 . (1, 12)
9 . (3, 0)
10 . (1, 5)
11 . (10, 2)
12 . (5, 9)
13 . (6, 11)
14 . (12, 16)
15 . (8, 14)
16 . (2, 7)
17 . (15, 4)
========================================
Verification test: 8G + 2G = 10G
8G + 2G = (1, 5)
"""
