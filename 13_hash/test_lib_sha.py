import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print("[ Explanation: using the custom Agama crypto library ]")

from crypto_agama.agama_transform_tools import hex_to_bin, num_to_bin
from crypto_agama.sha256py import Sha256py

print(Sha256py(b"Agama Point 209949850").hexdigest())

print("[ Explanation: using the standard Python cryptographic library ]")

# Example using Python's built-in 'hashlib' for SHA-256
import hashlib

msg = b"Agama Point 209949850"
print(hashlib.sha256(msg).hexdigest())


"""
[ Explanation: using the custom Agama crypto library ]
00000005434496a4937f988f644002737b4cda57137fd05f061690de6ca715a5
[ Explanation: using the standard Python cryptographic library ]
00000005434496a4937f988f644002737b4cda57137fd05f061690de6ca715a5
"""

