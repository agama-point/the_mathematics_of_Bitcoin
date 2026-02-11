"""
mini Merkle–Damgård | ASH16 = Agama simple hash 16 bit
ash16_test_2debug
"""

from ash24 import ASH24, bytes_to_bin24

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
        h = ASH24(data)

        if h in seen:
            for j in seen[h]:
                #print(f" {j}. 0x{j:x} | {i} (0x{i:x} |H| 0x{h:04x}")
                #print(bytes_to_bin16(bytes([1])))
                print(f" {j}. 0x{j:x} | {i} (0x{i:x} |H| 0x{h:04x} | bin {bytes_to_bin24(data)})")
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
for k in range(12,18):
    print("\n--- max_bits=", k, 2**k)
    find_collisions(k,True)

"""
--- max_bits= 15 32768
Collisions found: 0

--- max_bits= 16 65536
Collisions found: 0

--- 17
Collisions found: 500
--- 18 
Collisions found: 1525
"""