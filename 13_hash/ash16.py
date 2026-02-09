"""
mini Merkle–Damgård
ASH16 = Agama simple hash 16 bit
"""


def bytes_to_bin16(b: bytes) -> str:
    """Convert bytes to a 16-bit binary string (with leading zeros)."""
    s = ''.join(format(byte, '08b') for byte in b)
    return s.zfill(16)

    # print(format(x, '08b'))  # 00001111

def rol8(x, r):
    """Rotate an 8-bit value left by r bits"""
    return ((x << r) | (x >> (8 - r))) & 0xFF


def ASH16(data: bytes, debug=False):
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
    
    # A = B = C = 0

    # --- process input block by block (16 bits per block) ---
    for block_index in range(0, len(data), 2):
        m0 = data[block_index]
        m1 = data[block_index + 1]

        if debug:
            print("-"*12)
            print(f"\nBlock {block_index // 2}: {m0:02x} {m1:02x}")
            print(f"Initial state: A=0x{A:02x}, B=0x{B:02x}")

        # mix message block into the state (feed-forward)
        A ^= m0
        B ^= m1

        # --- mixing rounds ---
        num_rounds = 7

        for i in range(num_rounds):
            if debug:
                #print(f" r {i} | A=0x{A:02x} B=0x{B:02x} C=0x{B:02x}")
                print(f" r {i} | A={format(A,'08b')} B={format(B,'08b')} C={format(C,'08b')}")

            # cycle through IV8
            
            # --- AB ---
            """
            A ^= IV8[i % len(IV8)]
            A = rol8(A, 3)
            B = rol8(B, 2)  # &
            A ^= B          # diffusion step
            # A ^= ((B << 1) & 0xFF) | rol8(B, 2) # &&
            A, B = B, A     # swap registers
            """
            # --- ABC1 ---
            # A ^= IV8[i % len(IV8)]
            A ^= IV8[(i + block_index) % len(IV8)] # &&&
            B ^= rol8(C, 2)
            C ^= rol8(A, 3)
            # A = (A + B) & 0xFF # ABC2

            # diffusion
            A ^= B
            B ^= C
            C ^= A

            # swap-like rotation
            A, B, C = B, C, A
            # /ABC1 ---------------------------
            # ABC2
            """
            A = (A + IV8[(i + block_index) % len(IV8)]) & 0xFF
            
            # 2. ARX-like mixování
            A = (A + B) & 0xFF
            C ^= A
            C = rol8(C, 3)
            
            B = (B + C) & 0xFF
            A ^= B
            A = rol8(A, 2)
            
            # 3. Prohození pro další kolo
            A, B, C = B, C, A
            A ^= C
            B ^= rol8(C, 4)
            """

    # --- final 16-bit hash value ---
    return (A << 8) | B


def print_bit_hash(num):
    """
    Print the input number and its ASH16 hash
    - input: integer (0..65535+)
    - output: decimal and 16-bit binary representation
    """
    # minimal number of bytes to store the number
    nbytes = (num.bit_length() + 7) // 8 or 1
    data = num.to_bytes(nbytes, byteorder="big")
    h = ASH16(data)
    
    # pad input to 16-bit binary
    bin_input = ''.join(format(b,'08b') for b in data)
    bin_input = bin_input.zfill(16)
    
    # hash as 16-bit binary
    bin_hash = format(h, '016b')
    
    print(f"Input: {num} | bin: {bin_input} | Hash: {h} | bin: {bin_hash}")

