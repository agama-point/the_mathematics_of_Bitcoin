import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crypto_agama.agama_seed_tools import seed_words, mnemonic_info, words_to_bip39nums
from crypto_agama.agama_seed_tools import BIP39Functions, entropy_normalize, seed_words, mnemo_to_seed

bip39f = BIP39Functions()

print("-"*32)
print("[ --- test entropy --- ]")

def seed_test(entropy, passphrase=""):
    # entropy = entropy_normalize(entropy)
    print("input entropy:", entropy)
    phrase = bip39f.entropy_to_phrase(entropy)
    print("BIP39Functions - phrase:",phrase)
    print("is_valid | reverese_entropy:", bip39f.is_checksum_valid(phrase, reverse_entropy=True))
    mnemonic_info(phrase)
    return phrase

# ===================================================================
en_hex = "80808080808080808080808080808080"
words = seed_test(en_hex)
nums12 = words_to_bip39nums(words)

print("\n",nums12)

print("[mnemo_to_seed]")
seed = mnemo_to_seed(words)
print(seed)


# ============================
# Print 11-bit binary indices
# ============================

print("\n[ binary word indices ]")

word_list = words.split()   # list of BIP39 words
num_list = nums12           # corresponding numeric indices (0–2047)

for w, idx in zip(word_list, num_list):
    # convert index to fixed 11-bit binary string
    b11 = format(idx, "011b")
    # print binary, decimal index, and the word
    print(f"{b11:<12}  {idx:>4}   {w}")



"""
bip39 vectors: https://github.com/trezor/python-mnemonic/blob/master/vectors.json
"80808080808080808080808080808080"
"letter advice cage absurd amount doctor acoustic avoid letter advice cage above"

[ --- test entropy --- ]
input entropy: 80808080808080808080808080808080
BIP39Functions - phrase: letter advice cage absurd amount doctor acoustic avoid letter advice cage above
is_valid | reverese_entropy: (True, True, '80808080808080808080808080808080')
--------------------------------------------------------------------------------
[mnemonic_info]
letter advic...e cage above ( 12 )
1028 32 257 8 64 514 16 128 1028 32 257 4
validate:  (True, True)
--------------------------------------------------------------------------------
letter 1028 |advice 32 |cage 257 |absurd 8 |amount 64 |doctor 514 |acoustic 16 |avoid 128 |letter 1028 |advice 32 |cage 257 |above 4 |
 [1028, 32, 257, 8, 64, 514, 16, 128, 1028, 32, 257, 4]

[mnemo_to_seed]
b'e1N\xff9\x9d\x92\xa0\xdd\x066\x8d\xd6\x8ak\x8eae\xee\x95\xb0\x1b\xe9\xd8F\x00\xbdL2\xf6\x9b7\x08\xb4x\xbb\x9f!F5\x07~TD\xbf\xa42\xb2\xb9\x17\xb3\xc1cOJP\x9b\x03O\x99\xec\x86\xe5f' 

[ binary word indices ]
10000000100   1028   letter
00000100000     32   advice
00100000001    257   cage
00000001000      8   absurd
00001000000     64   amount
01000000010    514   doctor
00000010000     16   acoustic
00010000000    128   avoid
10000000100   1028   letter
00000100000     32   advice
00100000001    257   cage
00000000100      4   above
"""