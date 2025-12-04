import hashlib

# raw coinbase transaction from the genesis block
raw_tx_hex = (
    "01000000010000000000000000000000000000000000000000000000000000000000000000"
    "ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e"
    "63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062"
    "616e6b73ffffffff0100f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a"
    "828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a"
    "4c702b6bf11d5fac00000000"
)

# hex → bytes
raw_tx = bytes.fromhex(raw_tx_hex)

# 2x SHA256
merkle_root = hashlib.sha256(hashlib.sha256(raw_tx).digest()).digest()[::-1].hex()

print("Merkle root:", merkle_root)

"""
Merkle root: 4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b
"""
