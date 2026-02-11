"""
mini Merkle–Damgård
ASH24 = Agama simple hash 24 bit
"""

def bytes_to_bin24(b: bytes) -> str:
    """Convert bytes to a 16-bit binary string (with leading zeros)."""
    s = ''.join(format(byte, '08b') for byte in b)
    return s.zfill(24)

    # print(format(x, '08b'))  # 00001111

def rol8(x, r):
    """Rotate an 8-bit value left by r bits"""
    return ((x << r) | (x >> (8 - r))) & 0xFF


def ASH24(data: bytes, debug=False):
    """
    Simple 16-bit hash function ASH16
    - accepts input of arbitrary length
    - input is padded to a multiple of 16 bits (2 bytes)
    - processes input block-by-block
    """

    # --- IV8: fractional parts of square roots of the first 8 primes
    # (taken from SHA-256, truncated to 8 bits) ---
    IV8 = [
        0x6a,  # sqrt(2)
        0xbb,  # sqrt(3)
        0x3c,  # sqrt(5)
        0xa5,  # sqrt(7)
        0x51,  # sqrt(11)
        0x9b,  # sqrt(13)
        0x05,  # sqrt(17)
        0x1f,  # sqrt(19)
    ]
    """ ash24_iv8init.py:
    prime  2: 0x6a  01101010
    prime  3: 0xbb  10111011
    prime  5: 0x3c  00111100
    prime  7: 0xa5  10100101
    prime 11: 0x51  01010001
    prime 13: 0x9b  10011011
    prime 17: 0x1f  00011111
    """

    # --- pad input to a multiple of 16 bits (2 bytes) ---
    original_len = len(data)

    data += b"\x80"
    while (len(data) + 2) % 2 != 0: # Necháme místo 2 bajty na délku
        data += b"\x00"    
    data += original_len.to_bytes(2, "big")  # Přidání délky (16-bit integer na konec)
    """
    if original_len % 2 != 0:
        data += b"\x00"
    """
    if debug:
        print(f"Input after padding: {data.hex()}")

    # --- initial internal state ---
    A = IV8[0]
    B = IV8[1]
    C = IV8[2]
    # A = B = C = 0 # test

    # --- process input block by block (16 bits per block) ---
    for block_index in range(0, len(data), 2):
        m0 = data[block_index]
        m1 = data[block_index + 1]

        if debug:
            print("-"*12)
            print(f"\nBlock {block_index // 2}: {m0:02x} {m1:02x}")
            print(f"Initial state: A=0x{A:02x}, B=0x{B:02x}, C=0x{C:02x}")

        # mix message block into the state (feed-forward)
        A ^= m0
        B ^= m1
        C ^= (m0 + m1) & 0xFF

        # --- mixing rounds ---
        num_rounds = 16 ### 7/16 {17/18:500/2321->237/1527} 
        # rounds(bits):collisions ---> 15(15):3/(17):235, *16(17):237, 17(17):245

        for i in range(num_rounds):
            if debug:
                #print(f" r {i} | A=0x{A:02x} B=0x{B:02x} C=0x{B:02x}")
                print(f" r {i} | A={format(A,'08b')} B={format(B,'08b')} C={format(C,'08b')}")

            # cycle through IV8
            # --- ABC1 ---
            A ^= IV8[(i + block_index) % len(IV8)] # &&&
            B ^= rol8(C, 2)
            C ^= rol8(A, 3)
            A = (A + C) & 0xFF
            # --- ABC2 ---
            # A ^= m0 if i % 2 == 0 else m1 # Mix a piece of the message in every round
            # A ^= IV8[i % len(IV8)]
            # A = (A + IV8[(i + block_index) % len(IV8)]) & 0xFF
            # B = (B + A) & 0xFF  # B depends on the new A
            # C = (C ^ B)         # C changes via XOR with B
            # C = rol8(C, 3)      # Then C is mixed by rotation

            # diffusion
            A ^= B
            B ^= C
            C ^= A
            # swap-like rotation
            A, B, C = B, C, A

    # --- final 16-bit hash value ---
    # return (A << 8) | B
    # --- final 24-bit hash value ---
    if debug:
        print("="*12)
        print(f"Registers state: A=0x{A:02x}, B=0x{B:02x}, C=0x{C:02x}")
    return (A << 16) | (B << 8) | C

def print_bit_hash(num):
    """
    Print the input number and its ASH16 hash
    - input: integer (0..65535+)
    - output: decimal and 16-bit binary representation
    """
    # minimal number of bytes to store the number
    nbytes = (num.bit_length() + 7) // 8 or 1
    data = num.to_bytes(nbytes, byteorder="big")
    h = ASH24(data)
    
    # pad input to 16-bit binary
    bin_input = ''.join(format(b,'08b') for b in data)
    bin_input = bin_input.zfill(24)
    
    # hash as 16-bit binary
    bin_hash = format(h, '024b')
    hex_hash = f"{h:06x}"
    
    print(f"Input: {num} | bin: {bin_input} | Hash: {hex_hash} | bin: {bin_hash}")
