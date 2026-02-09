"""
mini Merkle–Damgård | ASH16 = Agama simple hash 16 bit
ash16_test_2debug
"""

from ash16 import ASH16, bytes_to_bin16

# =================================
def find_collisions(max_bits=16, find_all=False):
    """
    Find collisions for ASH16.
    - max_bits: number of bits of input to test
    - find_all: if True, print all collisions; otherwise, stop at first
    """
    seen = {}  # hash -> list of inputs that produced it
    collisions_found = 0

    for i in range(2**max_bits):
        # compute minimal number of bytes for the number
        nbytes = (i.bit_length() + 7) // 8
        data = i.to_bytes(nbytes, byteorder="big")
        h = ASH16(data)

        if h in seen:
            for j in seen[h]:
                #print(f" {j}. 0x{j:x} | {i} (0x{i:x} |H| 0x{h:04x}")
                #print(bytes_to_bin16(bytes([1])))
                print(f" {j}. 0x{j:x} | {i} (0x{i:x} |H| 0x{h:04x} | bin {bytes_to_bin16(data)})")
                collisions_found += 1
            seen[h].append(i)

            if not find_all:
                print(f"Stopping after first collision.")
                return

        else:
            seen[h] = [i]

    if find_all:
        print(f"Collisions found: {collisions_found}")


# =================================

print("-"*30)
for k in range(8,12):
    print("\n--- max_bits=", k, 2**k)
    find_collisions(k,True)

"""
--- max_bits= 8 256
Collisions found: 0

--- max_bits= 9 512
 240. 0xf0 | 325 (0x145 |H| 0xc384 | bin 0000000101000101)
Collisions found: 1

--- max_bits= 10 1024
 240. 0xf0 | 325 (0x145 |H| 0xc384 | bin 0000000101000101)
 24. 0x18 | 673 (0x2a1 |H| 0xdeb7 | bin 0000001010100001)
 191. 0xbf | 1021 (0x3fd |H| 0x2a59 | bin 0000001111111101)
Collisions found: 3

--- max_bits= 11 2048
 240. 0xf0 | 325 (0x145 |H| 0xc384 | bin 0000000101000101)
 24. 0x18 | 673 (0x2a1 |H| 0xdeb7 | bin 0000001010100001)
 191. 0xbf | 1021 (0x3fd |H| 0x2a59 | bin 0000001111111101)
 201. 0xc9 | 1128 (0x468 |H| 0xe4d1 | bin 0000010001101000)
 110. 0x6e | 1332 (0x534 |H| 0x103f | bin 0000010100110100)
 134. 0x86 | 1744 (0x6d0 |H| 0x0d0c | bin 0000011011010000)
 33. 0x21 | 1932 (0x78c |H| 0xf9e2 | bin 0000011110001100)
Collisions found: 7
"""