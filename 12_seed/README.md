# the_mathematics_of_Bitcoin

## 12) seed | BIP-39

```
code
```

---

### seed_from_entropy.py  — Inspecting BIP-39 entropy, word indices, and binary structure

This example demonstrates how raw entropy is converted into a valid BIP-39 mnemonic and how each word corresponds to an 11-bit index in the standardized 2048-word dictionary.
The script prints the input entropy, the resulting 12-word mnemonic, and then displays a table showing:

the 11-bit binary representation of each word index

the numeric index (0–2047)

the corresponding BIP-39 word

This allows you to inspect and verify how entropy is segmented into 11-bit groups, how checksum bits affect the last word, and how the mnemonic maps directly onto binary data.
The goal is to provide a transparent, step-by-step demonstration of the BIP-39 transformation pipeline:

entropy → entropy + checksum → 11-bit groups → word indices → mnemonic phrase

This is useful for testing custom implementations, validating third-party libraries, and understanding the low-level structure of the BIP-39 standard.

---

### seed_find_last.py  — Completing the 12th word so the checksum becomes valid

Another example demonstrates how to compute the final (12th) word when only the first 11 words are known.
Because a 12-word mnemonic contains 128 bits of entropy + 4 checksum bits, the last word is fully determined by:

the 7 high-order entropy bits of the 12th 11-bit group

the 4 checksum bits derived from SHA-256(entropy)

The script takes 11 known BIP-39 indices, reconstructs the partial entropy, calculates the correct checksum, and determines the only valid index for the last word.
This verifies the consistency of the checksum mechanism and shows that:

any 11-word prefix can be completed to exactly one valid 12-word mnemonic

the final checksum-constrained word is not arbitrary—it is mathematically enforced

brute-forcing the missing word is trivial (2048 options), but verifying correctness requires checksum validation

This example is valuable for teaching, security research, wallet debugging, and for demonstrating how BIP-39 checksum integrity prevents accidental word permutations from producing a valid seed.

---

