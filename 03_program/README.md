# the_mathematics_of_Bitcoin

## 03) Bitcoin Is a Program

Bitcoin can be understood as a **symbolic, rule-based programming language** executed collectively by a distributed network.  
Below is a simplified, high-level sketch of this “program” written in pseudocode-like form to illustrate the core logic.

---

### Initialization
```text
init
    generate random number
    transform to private key
    derive public key (ECC)
```

### Transaction Creation
```text
start
    build transaction
        load input addresses and BTC amounts
        define output addresses and amounts
        calculate transaction fee
        sign transaction with private key
```

### Broadcasting the Transaction
```text
send transaction to network
    connect to Bitcoin nodes
    broadcast transaction to peers
```

### Transaction Validation (at each node)
```text
if transaction is valid
    verify digital signature
    verify inputs are unspent (UTXO check)
    add transaction to mempool
else
    reject transaction
```

### Block Acceptance (by nodes)
```text
when node receives new block
    verify block validity
    verify all included transactions

    if block is valid
        append block to blockchain
        remove included transactions from mempool
    else
        reject block
```

### Block Acceptance (by nodes)
```text
when node receives new block
    verify block validity
    verify all included transactions

    if block is valid
        append block to blockchain
        remove included transactions from mempool
    else
        reject block
```

---

## This simplified flow shows Bitcoin as a deterministic program:

- Inputs are cryptographic keys and signed transactions
- Rules are enforced by every node independently
- State is shared via the blockchain
- Consensus emerges without central control

In this sense, Bitcoin is not just money—it is a globally replicated program whose execution defines monetary truth.




