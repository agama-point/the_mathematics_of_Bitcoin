#!/usr/bin/env python3
import struct
import binascii
import string

raw_tx_hex = (
    "01000000010000000000000000000000000000000000000000000000000000000000000000"
    "ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e"
    "63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062"
    "616e6b73ffffffff0100f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a"
    "828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a"
    "4c702b6bf11d5fac00000000"
)

# --- Helpers ---
def read_varint(data, offset):
    i = data[offset]
    offset += 1
    if i < 0xfd:
        return i, offset
    if i == 0xfd:
        val = struct.unpack_from('<H', data, offset)[0]
        return val, offset + 2
    if i == 0xfe:
        val = struct.unpack_from('<I', data, offset)[0]
        return val, offset + 4
    val = struct.unpack_from('<Q', data, offset)[0]
    return val, offset + 8

OPCODES = {
    0x00: 'OP_0',
    0x4c: 'OP_PUSHDATA1',
    0x4d: 'OP_PUSHDATA2',
    0x4e: 'OP_PUSHDATA4',
    0x6a: 'OP_RETURN',
    # small opcodes mapping for readability:
}
for i in range(1, 0x4c):
    OPCODES[i] = f'OP_PUSHBYTES({i})'
for i in range(0x51, 0x60):
    OPCODES[i] = f'OP_{i-0x50}'

def is_printable_ascii(bs):
    return all((chr(b) in string.printable and b not in (0x0a, 0x0d)) for b in bs)

def hexdump(bs):
    return bs.hex()

# --- Parse transaction ---
tx = bytes.fromhex(raw_tx_hex)
off = 0
version = struct.unpack_from('<I', tx, off)[0]; off += 4
print(f"version: {version} (0x{version:08x})")

# input count
vin_cnt, off = read_varint(tx, off)
print(f"vin_count: {vin_cnt}")

# parse first (and only) input
print("\n--- input[0] ---")
prev_txid = tx[off:off+32][::-1].hex(); off += 32
prev_vout = struct.unpack_from('<I', tx, off)[0]; off += 4
print(f"prev_txid: {prev_txid}")
print(f"prev_vout: {prev_vout}")

script_len, off = read_varint(tx, off)
print(f"script_length: {script_len} bytes")
script = tx[off:off+script_len]; off += script_len
sequence = tx[off:off+4]; off += 4
print(f"sequence: 0x{sequence.hex()}")

print("\n--- coinbase script (raw hex) ---")
print(script.hex())

# --- Disassemble script ---
print("\n--- disassembly (coinbase script) ---")
i = 0
while i < len(script):
    opcode = script[i]
    i += 1
    if opcode == 0x4c:  # OP_PUSHDATA1
        if i >= len(script):
            print("truncated OP_PUSHDATA1")
            break
        n = script[i]; i += 1
        data = script[i:i+n]; i += n
        tag = f"OP_PUSHDATA1 push {n} bytes"
    elif opcode == 0x4d:  # OP_PUSHDATA2
        if i + 1 >= len(script):
            print("truncated OP_PUSHDATA2")
            break
        n = struct.unpack_from('<H', script, i)[0]; i += 2
        data = script[i:i+n]; i += n
        tag = f"OP_PUSHDATA2 push {n} bytes"
    elif opcode == 0x4e:  # OP_PUSHDATA4
        if i + 3 >= len(script):
            print("truncated OP_PUSHDATA4")
            break
        n = struct.unpack_from('<I', script, i)[0]; i += 4
        data = script[i:i+n]; i += n
        tag = f"OP_PUSHDATA4 push {n} bytes"
    elif opcode <= 75:  # direct push OP_PUSHBYTES(opcode)
        n = opcode
        data = script[i:i+n]; i += n
        tag = f"OP_PUSHBYTES({n})"
    else:
        # Non-push opcode — print name if known
        opname = OPCODES.get(opcode, f'OP_UNKNOWN(0x{opcode:02x})')
        data = None
        tag = opname

    # print details
    print(f"{tag}:")
    if data is not None:
        print(f"  hex: {data.hex()}")
        if is_printable_ascii(data):
            try:
                print(f"  ascii: {data.decode('ascii')}")
            except Exception:
                pass
        # additionally try to interpret known fields:
        # detect nBits pattern (4 bytes, little-endian) near start
        if len(data) == 4 and 'nBits' not in globals():
            # (we won't set global, just print interpretation)
            val_le = int.from_bytes(data, 'little')
            print(f"  as little-endian hex: 0x{val_le:08x}")
    else:
        print(f"  opcode")

# After script, try to extract specifically the known fields from genesis layout
print("\n--- interpreted fields (expected for genesis) ---")
# According to genesis layout: script = (0xff.. markers) but we parse pushes above.
# We'll attempt to locate the nBits and the "The Times..." text programmatically.
# Search for ASCII "The Times"
ascii_idx = script.find(b"The Times")
if ascii_idx != -1:
    # find push header before it: backtrack to find length byte(s)
    start = ascii_idx
    # print surrounding bytes
    before = script[max(0, start-10):start]
    print(f"Found 'The Times' at script offset {ascii_idx}. Context bytes before: {before.hex()}")
    # decode the full pushed text length by reading the byte right before the ascii (push opcode)
    # naive approach: step backward to find a push opcode that indicates length
    # loop backward a few bytes
    for j in range(max(0, ascii_idx-10), ascii_idx):
        opcode = script[j]
        if opcode <= 75:
            length = opcode
            if j + 1 + length >= ascii_idx and script[j+1:j+1+length].startswith(b"The Times"):
                text = script[j+1:j+1+length]
                print(f"Detected push at offset {j}: pushlen={length}")
                print(f"Pushed ASCII text ({length} bytes):")
                print(text.decode('ascii'))
                break

# Also try to detect 4-byte nBits (pattern ffff001d)
nbits_offset = script.find(bytes.fromhex('ffff001d'))
if nbits_offset != -1:
    print(f"\nFound nBits pattern (ffff001d) at script offset {nbits_offset}")
    # show surrounding bytes
    ctx = script[max(0, nbits_offset-4):nbits_offset+8]
    print(f"context: {ctx.hex()}")

# extra nonce (0x04) is small push right after nBits in genesis
extra_nonce_offset = script.find(b'\x01\x04')
if extra_nonce_offset != -1:
    print(f"\nFound sequence 01 04 (push 1 byte with value 0x04) at offset {extra_nonce_offset}")
    print(f"bytes around: {script[extra_nonce_offset-4:extra_nonce_offset+6].hex()}")

# End
print("\nParsing complete.")


"""
version: 1 (0x00000001)
vin_count: 1

--- input[0] ---
prev_txid: 0000000000000000000000000000000000000000000000000000000000000000
prev_vout: 4294967295
script_length: 77 bytes
sequence: 0xffffffff

--- coinbase script (raw hex) ---
04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73

--- disassembly (coinbase script) ---
OP_PUSHBYTES(4):
  hex: ffff001d
  as little-endian hex: 0x1d00ffff
OP_PUSHBYTES(1):
  hex: 04
OP_PUSHBYTES(69):
  hex: 5468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73
  ascii: The Times 03/Jan/2009 Chancellor on brink of second bailout for banks

--- interpreted fields (expected for genesis) ---
Found 'The Times' at script offset 8. Context bytes before: 04ffff001d010445
Detected push at offset 7: pushlen=69
Pushed ASCII text (69 bytes):
The Times 03/Jan/2009 Chancellor on brink of second bailout for banks

Found nBits pattern (ffff001d) at script offset 1
context: 04ffff001d01044554

Found sequence 01 04 (push 1 byte with value 0x04) at offset 5
bytes around: ffff001d010445546865

Parsing complete.
"""
