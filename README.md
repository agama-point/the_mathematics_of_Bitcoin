# the_Mathematics_of_Bitcoin

### Mathematical Principles of the Bitcoin Revolution
### A Simplified Introduction to a Complex Topic
---
Learn how Bitcoin works under the hood: a practical dive into the algebra, number theory, and cryptography that make the network tick.

---
## install

```
git clone https://github.com/agama-point/the_mathematics_of_Bitcoin.git
cd the_mathematics_of_bitcoin
python3 -m venv venv  
source venv/bin/activate
pip install -r requirements.txt
touch .env
```

---

## Repository structure for `the_mathematics_of_Bitcoin`

Base: `https://github.com/agama-point/the_mathematics_of_Bitcoin/tree/main` :contentReference[oaicite:0]{index=0}

- 01 Bitcoin Is…
- 02 Bitcoin Needs a Computing Machine
- 03 Bitcoin Is a Computer Program | A Program Is a Sequence of Instructions
- [04_network](https://github.com/agama-point/the_mathematics_of_Bitcoin/tree/main/04_network)  Bitcoin Is a Transactional P2P Network | Computers in a Network — the Internet
- [05_code](https://github.com/agama-point/the_mathematics_of_Bitcoin/tree/main/05_code) Bitcoin Is Encoded Communication | Numeral Systems and Encoding
- 06 Bitcoin Is a Game with Large Numbers | Large Numbers Playing with “Infinity”
- [07_diffie_hellman](https://github.com/agama-point/the_mathematics_of_Bitcoin/tree/main/07_diffie_hellman) Asymmetric Cryptography | Diffie–Hellman Key Exchange
- [08_ecdh](https://github.com/agama-point/the_mathematics_of_Bitcoin/tree/main/08_ecdh) Elliptic Curves Are Elegant | Modular Arithmetic and Cyclic Groups
- [09_ecdsa](https://github.com/agama-point/the_mathematics_of_Bitcoin/tree/main/09_ecdsa) ECC Keys | ECDSA | secp256k1
- [10_grain_of_sand](https://github.com/agama-point/the_mathematics_of_Bitcoin/tree/main/10_grain_of_sand) Key Strength | Just a Grain of Sand in the Universe
- [11_entropy](https://github.com/agama-point/the_mathematics_of_Bitcoin/tree/main/11_entropy) How Important Is Entropy | Shannon Entropy
- [12_seed](https://github.com/agama-point/the_mathematics_of_Bitcoin/tree/main/12_seed) The Seed Is Your Key | How a Mnemonic Seed Is Created from a Random Number 
- [13_hash](https://github.com/agama-point/the_mathematics_of_Bitcoin/tree/main/13_hash) Grinding Data into Hashes | SHA-256
- 14 Merkle Trees Optimize Our Structure
- [15_address](https://github.com/agama-point/the_mathematics_of_Bitcoin/tree/main/15_address) Bitcoin Addresses Are Dynamic Account Numbers 
- [17_mining](https://github.com/agama-point/the_mathematics_of_Bitcoin/tree/main/17_mining) Bitcoin Mining Is Guessing a Number for a Reward | Finding the Nonce
- 18 The Blockchain Is an Unbreakable Chain | Conceptual Diagram
- 19 Halving Is a Clever Reduction of Miners’ Rewards
- [20_quantum_computer](https://github.com/agama-point/the_mathematics_of_Bitcoin/tree/main/20_quantum_computer) Quantum Computers | Basics 
- [21_quantum_threats](https://github.com/agama-point/the_mathematics_of_Bitcoin/tree/main/21_quantum_threats) The Threat of Quantum Computers to (B/b)itcoin?  
- [appendix_c](https://github.com/agama-point/the_mathematics_of_Bitcoin/tree/main/appendix_c) 
- [crypto_agama](https://github.com/agama-point/the_mathematics_of_Bitcoin/tree/main/crypto_agama)  
- [dot_env](https://github.com/agama-point/the_mathematics_of_Bitcoin/tree/main/dot_env)

---

## References

The examples in this repository use the library:  
https://github.com/agama-point/agama_point_crypto

Alternatively, you can use the older version (from 2020):  
https://github.com/agama-point/crypto_agama


A PyQt6-based desktop application for "secure" blockchain transactions using external hardware wallet devices connected via UART:
https://github.com/agama-point/obt_app

---

### Bitcoin Core (source code)  
**Repository:** https://github.com/bitcoin/bitcoin  
The Bitcoin Core repository contains the reference implementation of the Bitcoin protocol, including consensus rules, transaction processing, the P2P network layer, wallet primitives, and RPC/CLI tooling. It is the authoritative place to study how Bitcoin’s mathematical and cryptographic principles are implemented in real-world code.

### BIPs (Bitcoin Improvement Proposals)  
**Repository:** https://github.com/bitcoin/bips  
The BIPs repository hosts formal design documents that define standards, proposed protocol changes, and best practices for Bitcoin. Each BIP explains motivation, specification, and rationale, making this collection the primary source for understanding how the Bitcoin protocol evolves.

### trezor-common (well-engineered libraries)  
**Repository:** https://github.com/trezor/trezor-common  
The **trezor-common** project provides high-quality libraries and data structures used across Trezor hardware-wallet software. It offers practical examples of robust cryptographic implementations, serialization formats, and security-focused utilities built on top of Bitcoin’s core mathematical concepts.

---


## Support the Project

You can support the project with a Bitcoin on-chain payment to:  
`bc1q4sr56yf0awh2td28vzjdz2erl0tu7agama20sf`

One possible transaction link:  
https://chain.so/address/BTC/bc1q4sr56yf0awh2td28vzjdz2erl0tu7agama20sf
