# the_mathematics_of_Bitcoin

## 05) code

```
# This program converts a hexadecimal number ("ABC")
# first into decimal, then into binary.

h = "ABC"

# Convert hex → decimal
dec_value = int(h, 16)

# Convert decimal → binary (strip the "0b" prefix)
bin_value = bin(dec_value)[2:]

print("Hex:", h)
print("Dec:", dec_value)
print("Bin:", bin_value)
```

---


```
simple example | bin | hex | bech32
------------------------------
0 | 00000000000 | 0x0 | q
1 | 00000000001 | 0x1 | p
2 | 00000000010 | 0x2 | z
3 | 00000000011 | 0x3 | r
4 | 00000000100 | 0x4 | y
5 | 00000000101 | 0x5 | 9
6 | 00000000110 | 0x6 | x
7 | 00000000111 | 0x7 | 8
8 | 00000001000 | 0x8 | g
9 | 00000001001 | 0x9 | f
10 | 00000001010 | 0xa | 2
11 | 00000001011 | 0xb | t
12 | 00000001100 | 0xc | v
13 | 00000001101 | 0xd | d
14 | 00000001110 | 0xe | w
15 | 00000001111 | 0xf | 0
```

