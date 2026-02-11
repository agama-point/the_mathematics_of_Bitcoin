#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ess251
from ash24 import ASH24

def simple_hash(data):
    # return sum(data.encode()) % 0xFFFFFF
    return ASH24(data.encode())


def run_demo(debug_mode=False):
    print(f"\n--- RUNNING DEMO (Debug: {debug_mode}) ---")
    
    # 1. Setup Keys
    alice_priv = 111
    alice_pub = ess251.scalar_mult(alice_priv, ess251.G_POINT)
    if debug_mode:
        print("[DEBUG_1_SETUP]", alice_priv, alice_pub)
    
    # 2. Message and Hash
    msg = "Agama123"
    h = simple_hash(msg)
    if debug_mode:
       print("[DEBUG_2_MESSAGE_HASH]", msg, hex(h),"? js: 0x06eab2")

    # 3. Sign
    signature = ess251.sign(alice_priv, h, debug=debug_mode)
    
    # 4. Verify
    is_valid = ess251.verify(alice_pub, h, signature, debug=debug_mode)
    
    print(f"Final Result: {'Valid ✅' if is_valid else 'Invalid ❌'}")
    print("-"*30)
    print()
    # ---------- Bob -----------------
    bob_priv = 222
    bob_pub = ess251.scalar_mult(bob_priv, ess251.G_POINT)
    
    msg = "BobTest567"
    h = simple_hash(msg)
    if debug_mode:
       print("[DEBUG_1_SETUP]", bob_priv, bob_pub)
       print("[DEBUG_2_MESSAGE_HASH]", msg, hex(h),"? js: 0x20a8df")

    signature = ess251.sign(bob_priv, h, debug=debug_mode)
    is_valid = ess251.verify(bob_pub, h, signature, debug=debug_mode)
    print(f"Final Result: {'Valid ✅' if is_valid else 'Invalid ❌'}")


if __name__ == "__main__":
    print("=== AGAMA ECC SYSTEM INTERFACE ===")
    
    # Quiet run
    # run_demo(debug_mode=False)
    
    # Verbose run
    run_demo(debug_mode=True)

"""
=== AGAMA ECC SYSTEM INTERFACE ===

--- RUNNING DEMO (Debug: True) ---
[DEBUG_1_SETUP] 111 (131, 193)
[DEBUG_2_MESSAGE_HASH] Agama123 0x6eab2 ? js: 0x06eab2

[DEBUG-SIGN] Starting signing process...
[DEBUG-SIGN] Nonce k: 3
[DEBUG-SIGN] R-Point (k*G): (155, 235)
[DEBUG-SIGN] Signature components: r=155, s=249

[DEBUG-VERIFY] Starting verification process...
[DEBUG-VERIFY] Challenge e: 202
[DEBUG-VERIFY] L (s*G): (155, 16)
[DEBUG-VERIFY] P (R + e*PubKey): (155, 16)
Final Result: Valid ✅
------------------------------

[DEBUG_1_SETUP] 222 (232, 117)
[DEBUG_2_MESSAGE_HASH] BobTest567 0x20a8df ? js: 0x20a8df

[DEBUG-SIGN] Starting signing process...
[DEBUG-SIGN] Nonce k: 62
[DEBUG-SIGN] R-Point (k*G): (226, 107)
[DEBUG-SIGN] Signature components: r=226, s=188

[DEBUG-VERIFY] Starting verification process...
[DEBUG-VERIFY] Challenge e: 147
[DEBUG-VERIFY] L (s*G): (167, 195)
[DEBUG-VERIFY] P (R + e*PubKey): (167, 195)
Final Result: Valid ✅
"""