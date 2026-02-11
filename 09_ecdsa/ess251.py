#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ESS251: Elliptic Signature Scheme for p=251
A toy library for educational ECC purposes.
"""

# CURVE PARAMETERS
P_MOD = 251
A_PARAM = 0
B_PARAM = 7
G_POINT = (1, 192)
ORDER_N = 252

def inv_mod(x, mod):
    try:
        return pow(x, -1, mod)
    except ValueError:
        return None

def point_adding(P1, P2, p=P_MOD, a=A_PARAM):
    if P1 is None: return P2
    if P2 is None: return P1
    x1, y1 = P1
    x2, y2 = P2
    if x1 == x2 and y1 != y2:
        return None
    if x1 == x2:
        return point_doubling(P1, a, p)
    
    num = (y2 - y1) % p
    den = inv_mod(x2 - x1, p)
    if den is None: return None
    slope = (num * den) % p
    x3 = (slope**2 - x1 - x2) % p
    y3 = (slope * (x1 - x3) - y1) % p
    return (x3, y3)

def point_doubling(P, a=A_PARAM, p=P_MOD):
    if P is None: return None
    x, y = P
    if y == 0: return None
    num = (3 * x**2 + a) % p
    den = inv_mod(2 * y, p)
    if den is None: return None
    slope = (num * den) % p
    x3 = (slope**2 - 2 * x) % p
    y3 = (slope * (x - x3) - y) % p
    return (x3, y3)

def scalar_mult(k, P, a=A_PARAM, p=P_MOD, n=ORDER_N):
    result = None
    addend = P
    k = k % n
    while k > 0:
        if k & 1:
            result = point_adding(result, addend, p, a)
        addend = point_doubling(addend, a, p)
        k >>= 1
    return result

def sign(private_key, msg_hash, debug=False):
    if debug: print("\n[DEBUG-SIGN] Starting signing process...")
    
    # Deterministic nonce for demo
    k_nonce = (msg_hash ^ 0x55) % ORDER_N
    if k_nonce == 0: k_nonce = 1
    
    R_point = scalar_mult(k_nonce, G_POINT, A_PARAM, P_MOD, ORDER_N)
    r = R_point[0]
    e = msg_hash % ORDER_N
    s = (k_nonce + e * private_key) % ORDER_N
    
    if debug:
        print(f"[DEBUG-SIGN] Nonce k: {k_nonce}")
        print(f"[DEBUG-SIGN] R-Point (k*G): {R_point}")
        print(f"[DEBUG-SIGN] Signature components: r={r}, s={s}")
        
    return (r, s, R_point)

def verify(public_key_point, msg_hash, signature, debug=False):
    if debug: print("\n[DEBUG-VERIFY] Starting verification process...")
    r, s, R_point = signature
    e = msg_hash % ORDER_N
    
    # Verify: s*G = R + e*PubKey
    L = scalar_mult(s, G_POINT, A_PARAM, P_MOD, ORDER_N)
    e_Pub = scalar_mult(e, public_key_point, A_PARAM, P_MOD, ORDER_N)
    P = point_adding(R_point, e_Pub, P_MOD, A_PARAM)
    
    if debug:
        print(f"[DEBUG-VERIFY] Challenge e: {e}")
        print(f"[DEBUG-VERIFY] L (s*G): {L}")
        print(f"[DEBUG-VERIFY] P (R + e*PubKey): {P}")
    
    return L == P and L is not None