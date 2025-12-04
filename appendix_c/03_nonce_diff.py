#!/usr/bin/env python3
import hashlib
import binascii

# --- Genesis block header (80 bytes) ---
# version | prev_hash | merkle_root | time | bits | nonce
header_hex = (
    "01000000"
    "0000000000000000000000000000000000000000000000000000000000000000"
    "3ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a"
    "29ab5f49"
    "ffff001d"
    "1dac2b7c"
)

header = bytes.fromhex(header_hex)

# --- Helper: compute double SHA256 little-endian hash ---
def double_sha256(b):
    return hashlib.sha256(hashlib.sha256(b).digest()).digest()

# --- Decode target from nBits ---
def bits_to_target(bits_hex):
    bits = int(bits_hex, 16)
    exponent = bits >> 24
    mantissa = bits & 0xffffff

    # Bitcoin target formula
    target = mantissa * (1 << (8 * (exponent - 3)))
    return target

# nBits
bits_hex = "ffff001d"
target = bits_to_target(bits_hex)

print(f"nBits: {bits_hex}")
print(f"target:\n0x{target:064x}")

# --- Compute block hash ---
block_hash_le = double_sha256(header)
block_hash_int = int.from_bytes(block_hash_le, "little")

print("\nblock hash (little-endian):")
print(block_hash_le.hex())

print("\nblock hash (integer):")
print(f"0x{block_hash_int:064x}")

# --- Check difficulty ---
if block_hash_int <= target:
    print("\nOK: block hash satisfies difficulty target.")
else:
    print("\nFAIL: block hash does NOT satisfy difficulty!")

"""
block hash (little-endian):
6fe28c0ab6f1b372c1a6a246ae63f74f931e8365e15a089c68d6190000000000

block hash (integer):
0x000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f

OK: block hash satisfies difficulty target.
"""