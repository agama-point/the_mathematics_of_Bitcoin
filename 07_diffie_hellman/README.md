# the_mathematics_of_Bitcoin

## 07) Diffie-Hellman

```
# D-H simple xexample
g = 2   # Generator
p = 17  # Modulo prime number

# Alice and Bob choose their private keys
a = 5   # Alice's private key
b = 3   # Bob's private key

# Calculation of public keys
A = (g ** a) % p  # -> 15
B = (g ** b) % p  # -> 8

[a] private/secret | [A] public KEY
```

---

