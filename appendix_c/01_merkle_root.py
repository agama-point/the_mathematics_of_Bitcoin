import hashlib
from pathlib import Path
from textwrap import wrap

# ------------------------------------------------------------
# Genesis block Merkle root verification
# ------------------------------------------------------------

print("STEP 1: Locate genesis_block.txt")

BASE_DIR = Path(__file__).resolve().parent
block_path = BASE_DIR / "genesis_block.txt"

print("Block file:", block_path)

# ------------------------------------------------------------
# Load block
# ------------------------------------------------------------

print("\nSTEP 2: Load full genesis block (hex)")

with open(block_path, "r") as f:
    block_hex = f.read().strip()

print("Total block hex length:", len(block_hex))

# ------------------------------------------------------------
# Parse block header (80 bytes)
# ------------------------------------------------------------

print("\nSTEP 3: Parse block header")

offset = 0

def read_bytes(n):
    global offset
    size = n * 2
    value = block_hex[offset:offset + size]
    offset += size
    return value

version_hex = read_bytes(4)
prev_block_hex = read_bytes(32)
merkle_root_hex = read_bytes(32)
time_hex = read_bytes(4)
bits_hex = read_bytes(4)
nonce_hex = read_bytes(4)

print("Version:            ", version_hex)
print("Previous block:     ", prev_block_hex)
print("Merkle root (raw):  ", merkle_root_hex)
print("Time:               ", time_hex)
print("Bits:               ", bits_hex)
print("Nonce:              ", nonce_hex)

# Store expected Merkle root (convert to human-readable big endian)
expected_merkle_root = bytes.fromhex(merkle_root_hex)[::-1].hex()

print("\nExpected Merkle root (from header):")
print(expected_merkle_root)

# ------------------------------------------------------------
# Parse transaction count (varint)
# ------------------------------------------------------------

print("\nSTEP 4: Parse transaction count (varint)")

tx_count_hex = read_bytes(1)
tx_count = int(tx_count_hex, 16)

print("Transaction count:", tx_count)

if tx_count != 1:
    raise ValueError("Genesis block must contain exactly 1 transaction")

# ------------------------------------------------------------
# Extract raw coinbase transaction
# ------------------------------------------------------------

print("\nSTEP 5: Extract raw coinbase transaction")

tx_hex = block_hex[offset:]

print("Coinbase TX hex length:", len(tx_hex))

print("\nCoinbase transaction (32 hex chars per line):\n")
for line in wrap(tx_hex, 32):
    print(line)

tx_bytes = bytes.fromhex(tx_hex)
print("\nCoinbase TX byte length:", len(tx_bytes))

# ------------------------------------------------------------
# Compute Merkle root
# ------------------------------------------------------------

print("\nSTEP 6: Compute double SHA256 of coinbase TX")

hash1 = hashlib.sha256(tx_bytes).digest()
hash2 = hashlib.sha256(hash1).digest()

computed_merkle_root = hash2[::-1].hex()

print("SHA256 #1:", hash1.hex())
print("SHA256 #2:", hash2.hex())

# ------------------------------------------------------------
# Compare results
# ------------------------------------------------------------

print("\nSTEP 7: Compare Merkle roots")

print("Expected (from header):", expected_merkle_root)
print("Computed (from TX):    ", computed_merkle_root)

if expected_merkle_root == computed_merkle_root:
    print("\nRESULT: OK — Merkle root matches")
else:
    print("\nRESULT: ERROR — Merkle root does NOT match")




"""

"""
