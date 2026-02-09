# the_mathematics_of_Bitcoin

## 13) Hash

```
nonce = 209949850 -> "Agama Point 209949850":
[ Explanation: using the custom Agama crypto library ]
00000005434496a4937f988f644002737b4cda57137fd05f061690de6ca715a5
[ Explanation: using the standard Python cryptographic library ]      
00000005434496a4937f988f644002737b4cda57137fd05f061690de6ca715a5
```

---


Explanation:
```
-------------------- [ abcdefgh vector ] abc -> hs 
0.4142135624     1779033703      01101010000010011110011001100111
0.7320508076     3144134277      10111011011001111010111010000101
0.2360679775     1013904242      00111100011011101111001101110010
0.6457513111     2773480762      10100101010011111111010100111010
0.3166247904     1359893119      01010001000011100101001001111111
0.6055512755     2600822924      10011011000001010110100010001100
0.1231056256     528734635       00011111100000111101100110101011
0.3588989435     1541459225      01011011111000001100110100011001
-------------------- [ test ]
0x6a09e667 01101010000010011110011001100111
0xbb67ae85 10111011011001111010111010000101
0x3c6ef372 00111100011011101111001101110010
0xa54ff53a 10100101010011111111010100111010
0x510e527f 01010001000011100101001001111111
0x9b05688c 10011011000001010110100010001100
0x1f83d9ab 00011111100000111101100110101011
0x5be0cd19 01011011111000001100110100011001
-------------------- [ ks vector ] first 5 norm_sqr()
2        0.2599210499    1116352408      0x428a2f98      01000010100010100010111110011000
3        0.4422495703    1899447441      0x71374491      01110001001101110100010010010001
5        0.7099759467    3049323471      0xb5c0fbcf      10110101110000001111101111001111
7        0.9129311828    3921009573      0xe9b5dba5      11101001101101011101101110100101
11       0.2239800906    961987163       0x3956c25b      00111001010101101100001001011011
0x428a2f98 01000010100010100010111110011000
0x71374491 01110001001101110100010010010001
0xb5c0fbcf 10110101110000001111101111001111
0xe9b5dba5 11101001101101011101101110100101
0x3956c25b 00111001010101101100001001011011

-------------------- [ maj ]
x 0x6a09e667 01101010000010011110011001100111
y 0xbb67ae85 10111011011001111010111010000101
z 0x3c6ef372 00111100011011101111001101110010
==================================================
> 0x3a6fe667 00111010011011111110011001100111

-------------------- [ ch ]
x 0x6a09e667 01101010000010011110011001100111
y 0xbb67ae85 10111011011001111010111010000101
z 0x3c6ef372 00111100011011101111001101110010
==================================================
> 0x3e67b715 00111110011001111011011100010101

-------------------- [ ror ]
x 0x6a09e667 01101010000010011110011001100111
==================================================
1 0xb504f333 10110101000001001111001100110011
2 0xda827999 11011010100000100111100110011001
5 0x3b504f33 00111011010100000100111100110011
7 0xced413cc 11001110110101000001001111001100
```

---

# ASH16 – Agama Simple Hash (16-bit)

**ASH16** is a small, educational 16-bit hash function designed to illustrate the principles of cryptographic hashing in a highly simplified setting. It is **not intended for secure cryptographic use** but serves as a minimalistic model for teaching and experimentation.

## What it Does

ASH16 takes an arbitrary-length input (sequence of bytes) and produces a fixed **16-bit hash value**. It processes the input in **16-bit blocks**, using an internal state of 2–3 8-bit registers (`A`, `B`, optionally `C`) and simple operations such as XOR, rotations, and swapping.

## How It Works

1. **Input Padding**  
   - The input is padded with zeros to a multiple of 16 bits (2 bytes) so that each block can be processed consistently.

2. **Initial State**  
   - The internal registers are initialized to zero (`A = 0x00`, `B = 0x00`, optional `C = 0x00`).  
   - A small **initial vector (`IV8`)** derived from the fractional parts of the square roots of the first 8 primes (truncated to 8 bits) is used for mixing.

3. **Block Processing**  
   - Each 16-bit block of the input is split into two bytes (`m0`, `m1`).  
   - The bytes are **mixed into the internal state** using XOR operations with the registers.

4. **Mixing Rounds**  
   - The function performs several rounds (e.g., 8–16) of **mixing**, where each round:
     - XORs a register with an IV element (cycling through `IV8` if rounds > 8)  
     - Applies **rotations** (`rol8`) to `A` and `B`  
     - Combines registers using XOR and other small diffusion operations  
     - Swaps the registers to propagate differences

5. **Output**  
   - After processing all blocks, the final state of registers `A` and `B` (and optionally `C`) is combined into a **16-bit hash**.  
   - The hash can be output in **decimal, hexadecimal, or binary form** for inspection.

## Why It Works

- The small internal state and repeated mixing rounds allow input bits to **diffuse** across the registers.  
- XOR and rotations provide a simple nonlinear transformation, demonstrating how small differences in input produce changes in the hash output.  
- Cycling through `IV8` ensures that even repetitive inputs produce varying intermediate states.  

## Educational Purpose

ASH16 is a **teaching tool** for understanding:

- Padding and block processing in hash functions  
- Register-based internal state updates  
- Basic diffusion through XOR, rotation, and swapping  
- The inevitability of collisions in small hash sizes (16 bits)  

It is **not secure** and should not be used for any real cryptographic applications. Its simplicity makes it ideal for **experiments with collisions, hash visualization, and bit-level debugging**.

---

### Optional Diagram (Conceptual)
```text
Input block (16 bits)
│
▼
+----------------+
| Registers A,B |
| Optional C |
+----------------+
│
▼
[8-16 Mixing Rounds: XOR, ROT, Swap, IV8]
│
▼
16-bit ASH16 Hash Output
```

# ASH16 – Agama Simple Hash (16-bit)

**ASH16** is a small, educational 16-bit hash function designed to illustrate the principles of cryptographic hashing in a highly simplified setting. It is **not intended for secure cryptographic use** but serves as a minimalistic model for teaching and experimentation.

## What it Does

ASH16 takes an arbitrary-length input (sequence of bytes) and produces a fixed **16-bit hash value**. It processes the input in **16-bit blocks**, using an internal state of 2–3 8-bit registers (`A`, `B`, optionally `C`) and simple operations such as XOR, rotations, and swapping.

## How It Works

1. **Input Padding**  
   - The input is padded with zeros to a multiple of 16 bits (2 bytes) so that each block can be processed consistently.

2. **Initial State**  
   - The internal registers are initialized to zero (`A = 0x00`, `B = 0x00`, optional `C = 0x00`).  
   - A small **initial vector (`IV8`)** derived from the fractional parts of the square roots of the first 8 primes (truncated to 8 bits) is used for mixing.

3. **Block Processing**  
   - Each 16-bit block of the input is split into two bytes (`m0`, `m1`).  
   - The bytes are **mixed into the internal state** using XOR operations with the registers.

4. **Mixing Rounds**  
   - The function performs several rounds (e.g., 8–16) of **mixing**, where each round:
     - XORs a register with an IV element (cycling through `IV8` if rounds > 8)  
     - Applies **rotations** (`rol8`) to `A` and `B`  
     - Combines registers using XOR and other small diffusion operations  
     - Swaps the registers to propagate differences

5. **Output**  
   - After processing all blocks, the final state of registers `A` and `B` (and optionally `C`) is combined into a **16-bit hash**.  
   - The hash can be output in **decimal, hexadecimal, or binary form** for inspection.

## Binary Visualization

To better understand how input propagates through the hash function, ASH16 can be represented **bitwise**:

```text
AB:
Input:  00000001 00000000  (16-bit block)
Registers A,B (initial): 00000000 00000000

Round 0:
  A ^= IV8[0]  -> 10101010
  B rotated    -> 00000000
  A ^= B       -> 10101010
  Swap A,B     -> 00000000 10101010

Round 1:
  ...
  
Final Hash Output (16-bit):
  10101010 11001100
```


```text
ABC:
Input:  00000001 00000000  (16-bit block)
Registers A,B (initial): 00000000 00000000

Round 0:
  A ^= IV8[0]  -> 10101010
  B rotated    -> 00000000
  A ^= B       -> 10101010
  Swap A,B     -> 00000000 10101010

Round 1:
  ...
  
Final Hash Output (16-bit):
  10101010 11001100
```
```python
print_bit_hash(1)
print_bit_hash(256)
print_bit_hash(1023)
print_bit_hash(0xABCD)
```
```
Input: 1 | bin: 0000000000000001 | Hash: 46660 | bin: 1011011001000100
Input: 256 | bin: 0000000100000000 | Hash: 46660 | bin: 1011011001000100
Input: 1023 | bin: 0000001111111111 | Hash: 52345 | bin: 1100110010101001
Input: 43981 | bin: 1010101111001101 | Hash: 34121 | bin: 1000010100111001
```




