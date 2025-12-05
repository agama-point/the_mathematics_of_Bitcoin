import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from crypto_agama.agama_transform_tools import hex_to_bin, num_to_bin

from crypto_agama.diffie_hellman import DiffieHellmanKeys

G = 2 # generator
p = 17

# Alice and Bob choose their private keys
a = 5  # Alice's private key
b = 3  # Bob's private key

# Create an instance of the DiffieHellmanKeys class
"""
dh_a = DiffieHellmanKeys(3,17) # test small g, p
print(dh_a) # basic info
print("is_primitive_root:",dh_a.is_primitive_root(3, 17 )) # True
"""

dh_a = DiffieHellmanKeys(G,p)
dh_b = DiffieHellmanKeys(G,p)

print("[ Parameters ]")
print("prime/modulo: ", dh_a.p)
print("---generator: ", dh_a.g)

print("[ Private keys ] a, b :")
print(a,b)

print("=" * 30)
print("[ --- Alice --- ]")
alice_private_key = a
alice_public_key = dh_a.generate_public_key(alice_private_key)
print(f'Private key: {(alice_private_key)} | {hex(alice_private_key)}\nPublic key: {hex(alice_public_key)}')

print()
print("[ --- Bob --- ]")
bob_private_key = b
bob_public_key = dh_b.generate_public_key(bob_private_key)
print(f'Private key: {bob_private_key} | {hex(bob_private_key)}\nPublic key: {hex(bob_public_key)}')

print("-" * 30)
print("Confirm")
alice_shared_secret = dh_a.generate_shared_secret(alice_private_key, bob_public_key)
bob_shared_secret = dh_b.generate_shared_secret(bob_private_key, alice_public_key)

print()
print("-" * 30)
print("[ Shared secrets ]")
print(f'A:  {alice_shared_secret}')
print(f'B:  {bob_shared_secret}')

assert alice_shared_secret == bob_shared_secret, "Shared secrets do not match!"
print("Shared secrets match.")

hex32 = dh_a.get_hex_shared32()
print(f"{hex32}  ({len(hex32)})")


"""
[ Parameters ]
prime/modulo:  17
---generator:  2
[ Private keys ] a, b :
5 3
==============================
[ --- Alice --- ]
Private key: 5 | 0x5
Public key: 0xf

[ --- Bob --- ]
Private key: 3 | 0x3
Public key: 0x8
------------------------------
Confirm
"""
