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

"""
DiffieHellmanKeys
(g = 2, p = 17)

[ Parameters ]
prime/modulo:  17
---generator:  2
[ --- Alice --- ]
Public key: 15
"""
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
[ Parameters ]
prime/modulo:  170141183460469231731687303715884105727
---generator:  3
[ Private keys ] a, b :
555555555555 333333333333
==============================
[ --- Alice --- ]
Private key: 555555555555 | 0x8159b108e3
Public key: 0x236d61d241c8deec988b449371ef59fb

[ --- Bob --- ]
Private key: 333333333333 | 0x4d9c370555
Public key: 0x20119b431bf77946dab17b2056cacf56
------------------------------
Confirm

------------------------------
[ Shared secrets ]
A:  145101968037071639412442679777990239948
B:  145101968037071639412442679777990239948
Shared secrets match.
6d299f5dae62c2e9c9f2806ae9ab66cc  (32)
================================
6d299f5dae62c2e9c9f2806ae9ab66cc
"""
...
```


