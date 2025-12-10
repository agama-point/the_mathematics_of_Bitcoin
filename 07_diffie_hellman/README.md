# the_mathematics_of_Bitcoin

## 07) Diffie-Hellman

```
# D-H simple example
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

Example use of a simple Agama library:

```python
from crypto_agama.diffie_hellman import DiffieHellmanKeys

G = 2 # generator
p = 17

dh = DiffieHellmanKeys(G,p)
print(dh) # basic info

print("[ Parameters ]")
print("prime/modulo: ", dh.p)
print("---generator: ", dh.g)

print("[ --- Alice --- ]")
alice_private_key = 5
alice_public_key = dh.generate_public_key(alice_private_key)
...
# 15

```

---

```python
...
dh = DiffieHellmanKeys()
sk = 555555555555
pk = dh.generate_public_key(sk)
ss = dh.generate_shared_secret(sk, bob_public_key) 
print(dh.get_hex_shared32())

"""
================================
568a721168e50d5665cf5cd889c52235
"""
...
```


