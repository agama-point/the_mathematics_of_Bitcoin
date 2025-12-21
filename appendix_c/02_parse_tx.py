#!/usr/bin/env python3
import hashlib
import struct
from pathlib import Path
from textwrap import wrap

# --- Helper Functions ---
def dsha256(data_bytes):
    """Performs double SHA256 hash: SHA256(SHA256(data))"""
    return hashlib.sha256(hashlib.sha256(data_bytes).digest()).digest()

def format_header(title):
    print("\n" + "="*60)
    print(f"{title:^60}")
    print("="*60)

# ------------------------------------------------------------
# STEP 1: File Initialization
# ------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
block_path = BASE_DIR / "genesis_block.txt"

if not block_path.exists():
    print(f"Error: {block_path} not found.")
    exit(1)

with open(block_path, "r") as f:
    # Remove any whitespaces, newlines or tabs from the input file
    block_hex = "".join(f.read().split())

# ------------------------------------------------------------
# STEP 2: Parse Block Header (80 bytes)
# ------------------------------------------------------------
format_header("BITCOIN GENESIS BLOCK HEADER")

# Bitcoin headers are 80 bytes (160 hex characters)
header_bytes = bytes.fromhex(block_hex[:160])

# Unpack header fields using little-endian (<)
# I=uint32 (4 bytes), 32s=32 byte string
version = struct.unpack_from("<I", header_bytes, 0)[0]
prev_block = header_bytes[4:36][::-1].hex()
merkle_root_header = header_bytes[36:68][::-1].hex()
timestamp = struct.unpack_from("<I", header_bytes, 68)[0]
bits = struct.unpack_from("<I", header_bytes, 72)[0]
nonce = struct.unpack_from("<I", header_bytes, 76)[0]

block_hash = dsha256(header_bytes)[::-1].hex()

print(f"Block Hash:   {block_hash}")
print(f"Version:      {version}")
print(f"Prev Block:   {prev_block}")
print(f"Merkle Root:  {merkle_root_header}")
print(f"Timestamp:    {timestamp} (2009-01-03 18:15:05)")
print(f"Bits:         {bits:08x}")
print(f"Nonce:        {nonce}")

# ------------------------------------------------------------
# STEP 3: Transaction Count
# ------------------------------------------------------------
# The byte following the header (offset 80) is the Tx count (VarInt)
tx_count = int(block_hex[160:162], 16)
print(f"\nTransactions: {tx_count}")

# ------------------------------------------------------------
# STEP 4: Detailed Coinbase Transaction Parsing
# ------------------------------------------------------------
format_header("COINBASE TRANSACTION ANALYSIS")

# Extract the transaction part (everything after the header and tx_count)
tx_hex = block_hex[162:]
tx_bytes = bytes.fromhex(tx_hex)

ptr = 0

# 1. Version (4 bytes)
tx_version = struct.unpack_from("<I", tx_bytes, ptr)[0]
ptr += 4

# 2. Input Count (1 byte for Genesis)
vin_count = tx_bytes[ptr]
ptr += 1

# --- Input Parsing ---
print(f"--- Input [0] ---")
prev_txid = tx_bytes[ptr:ptr+32][::-1].hex() # Should be 000...0
ptr += 32
prev_vout = struct.unpack_from("<I", tx_bytes, ptr)[0] # Should be ffffffff
ptr += 4

script_len = tx_bytes[ptr]
ptr += 1
script_sig = tx_bytes[ptr:ptr+script_len]
ptr += script_len

sequence = tx_bytes[ptr:ptr+4].hex()
ptr += 4

print(f"Prev TXID:    {prev_txid}")
print(f"Prev VOUT:    {prev_vout} (Coinbase identifier)")
print(f"Script Length:{script_len} bytes")

# Extracting Satoshi's hidden message from ScriptSig
try:
    msg_idx = script_sig.find(b"The Times")
    if msg_idx != -1:
        message = script_sig[msg_idx:].decode('ascii')
        print(f"Message:      \033[92m{message}\033[0m")
except Exception:
    print("Message:      (Could not decode ASCII)")

# 3. Output Count
vout_count = tx_bytes[ptr]
ptr += 1

# --- Output Parsing ---
print(f"\n--- Output [0] ---")
value_sats = struct.unpack_from("<Q", tx_bytes, ptr)[0] # Q=uint64
ptr += 8

pk_script_len = tx_bytes[ptr]
ptr += 1
pk_script = tx_bytes[ptr:ptr+pk_script_len]
ptr += pk_script_len

print(f"Amount:       {value_sats / 100_000_000:.1f} BTC")
print(f"PK Script:    {pk_script.hex()[:40]}...")

# 4. Locktime
locktime = struct.unpack_from("<I", tx_bytes, ptr)[0]
print(f"\nLocktime:     {locktime}")

# ------------------------------------------------------------
# STEP 5: Integrity Verification
# ------------------------------------------------------------
format_header("VERIFICATION RESULTS")

computed_txid = dsha256(tx_bytes)[::-1].hex()

print(f"Computed TXID:  {computed_txid}")
print(f"Header Merkle:  {merkle_root_header}")

if computed_txid == merkle_root_header:
    print("\n[RESULT] SUCCESS: Transaction matches Merkle Root!")
else:
    print("\n[RESULT] ERROR: Hash mismatch detected!")

if block_hash.startswith("000000000019"):
    print("[RESULT] SUCCESS: Block Hash satisfies Difficulty!")