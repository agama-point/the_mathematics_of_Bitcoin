#!/usr/bin/env python3
import hashlib
import struct
from pathlib import Path

def calculate_dsha256(data):
    """Returns the double SHA256 hash of the input data."""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

def get_target_from_bits(bits_int):
    """
    Converts nBits (compact format) to the 256-bit target integer.
    Formula: target = mantissa * 2^(8 * (exponent - 3))
    """
    exponent = bits_int >> 24
    mantissa = bits_int & 0x00ffffff
    target = mantissa * (256 ** (exponent - 3))
    return target

def main():
    # 1. Load raw data from the local txt file
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir / "genesis_block.txt"
    
    try:
        with open(file_path, "r") as f:
            hex_string = "".join(f.read().split())
        raw_data = bytes.fromhex(hex_string)
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # 2. Extract Header Fields (First 80 bytes)
    # nBits offset: 72-76 | Nonce offset: 76-80
    header = raw_data[:80]
    nbits = struct.unpack("<I", header[72:76])[0]
    nonce = struct.unpack("<I", header[76:80])[0]

    # 3. Calculate Proof of Work Metrics
    target = get_target_from_bits(nbits)
    block_hash_le = calculate_dsha256(header)
    
    # We interpret the hash as a little-endian integer to compare with Target
    hash_int = int.from_bytes(block_hash_le, "little")
    hash_hex_be = block_hash_le[::-1].hex()

    # 4. Display Results
    print("=" * 65)
    print(f"{'MINING & DIFFICULTY REPORT':^65}")
    print("=" * 65)
    
    print(f"nBits (Hex):      0x{nbits:08x}")
    print(f"Nonce (Decimal):  {nonce}")
    print(f"Nonce (Hex):      0x{nonce:08x}")
    
    print(f"\nDifficulty Target:")
    print(f"0x{target:064x}")
    
    print(f"\nActual Block Hash:")
    print(f"0x{hash_int:064x}")
    print(f"({hash_hex_be})")
    
    print("-" * 65)
    
    # The golden rule of Bitcoin mining: Hash <= Target
    if hash_int <= target:
        print("STATUS: SUCCESS")
        print("The hash is LOWER than the target. Proof of Work is VALID.")
    else:
        print("STATUS: FAILED")
        print("The hash is HIGHER than the target. Proof of Work is INVALID.")
    print("-" * 65)

if __name__ == "__main__":
    main()