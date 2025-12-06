# the_mathematics_of_Bitcoin
Learn how Bitcoin works under the hood: a practical dive into the algebra, number theory, and cryptography that make the network tick.

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

## Libraries Used

The examples in this repository use the library:  
https://github.com/agama-point/agama_point_crypto

Alternatively, you can use the older version (from 2020):  
https://github.com/agama-point/crypto_agama

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
