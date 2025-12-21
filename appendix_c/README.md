# the_mathematics_of_Bitcoin

## Appendix C - the genesis block

```
00000000   01 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00   ................
00000010   00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00   ................
00000020   00 00 00 00 3B A3 ED FD  7A 7B 12 B2 7A C7 2C 3E   ....;£íýz{.²zÇ,>
00000030   67 76 8F 61 7F C8 1B C3  88 8A 51 32 3A 9F B8 AA   gv.a.È.ÃˆŠQ2:Ÿ¸ª
00000040   4B 1E 5E 4A 29 AB 5F 49  FF FF 00 1D 1D AC 2B 7C   K.^J)«_Iÿÿ...¬+|
00000050   01 01 00 00 00 01 00 00  00 00 00 00 00 00 00 00   ................
00000060   00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00   ................
00000070   00 00 00 00 00 00 FF FF  FF FF 4D 04 FF FF 00 1D   ......ÿÿÿÿM.ÿÿ..
00000080   01 04 45 54 68 65 20 54  69 6D 65 73 20 30 33 2F   ..EThe Times 03/
00000090   4A 61 6E 2F 32 30 30 39  20 43 68 61 6E 63 65 6C   Jan/2009 Chancel
000000A0   6C 6F 72 20 6F 6E 20 62  72 69 6E 6B 20 6F 66 20   lor on brink of 
000000B0   73 65 63 6F 6E 64 20 62  61 69 6C 6F 75 74 20 66   second bailout f
000000C0   6F 72 20 62 61 6E 6B 73  FF FF FF FF 01 00 F2 05   or banksÿÿÿÿ..ò.
000000D0   2A 01 00 00 00 43 41 04  67 8A FD B0 FE 55 48 27   *....CA.gŠý°þUH'
000000E0   19 67 F1 A6 71 30 B7 10  5C D6 A8 28 E0 39 09 A6   .gñ¦q0·.\Ö¨(à9.¦
000000F0   79 62 E0 EA 1F 61 DE B6  49 F6 BC 3F 4C EF 38 C4   ybàê.aÞ¶Iö¼?Lï8Ä
00000100   F3 55 04 E5 1E C1 12 DE  5C 38 4D F7 BA 0B 8D 57   óU.å.Á.Þ\8M÷º..W
00000110   8A 4C 70 2B 6B F1 1D 5F  AC 00 00 00 00            ŠLp+kñ._¬....
```
---

```
01 merkle root - validation
02 parse coinbase transaction from the genesis block
03 nonce and difficulty
```

---
### 01_merkle_root.py

```
STEP 1: Locate genesis_block.txt
Block file: D:\data_matematika_b\github\appendix_c\genesis_block.txt

STEP 2: Load full genesis block (hex)
Total block hex length: 570

STEP 3: Parse block header
Version:             01000000
Previous block:      0000000000000000000000000000000000000000000000000000000000000000
Merkle root (raw):   3BA3EDFD7A7B12B27AC72C3E67768F617FC81BC3888A51323A9FB8AA4B1E5E4A
Time:                29AB5F49
Bits:                FFFF001D
Nonce:               1DAC2B7C

Expected Merkle root (from header):
4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b

STEP 4: Parse transaction count (varint)
Transaction count: 1

STEP 5: Extract raw coinbase transaction
Coinbase TX hex length: 408

Coinbase transaction (32 hex chars per line):

01000000010000000000000000000000 00000000000000000000000000000000
0000000000FFFFFFFF4D04FFFF001D01 04455468652054696D65732030332F4A
616E2F32303039204368616E63656C6C 6F72206F6E206272696E6B206F662073
65636F6E64206261696C6F757420666F 722062616E6B73FFFFFFFF0100F2052A
01000000434104678AFDB0FE55482719 67F1A67130B7105CD6A828E03909A679
62E0EA1F61DEB649F6BC3F4CEF38C4F3 5504E51EC112DE5C384DF7BA0B8D578A
4C702B6BF11D5FAC00000000

Coinbase TX byte length: 204

STEP 6: Compute double SHA256 of coinbase TX
SHA256 #1: 27362e66e032c731c1c8519f43063fe0e5d070db1c0c3552bb04afa18a31c6bf
SHA256 #2: 3ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a

STEP 7: Compare Merkle roots
Expected (from header): 4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b
Computed (from TX):     4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b

RESULT: OK — Merkle root matches
```

---
### 02_parse_tx.py

```
============================================================
                BITCOIN GENESIS BLOCK HEADER
============================================================
Block Hash:   000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
Version:      1
Prev Block:   0000000000000000000000000000000000000000000000000000000000000000
Merkle Root:  4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b
Timestamp:    1231006505 (2009-01-03 18:15:05)
Bits:         1d00ffff
Nonce:        2083236893

Transactions: 1

============================================================
               COINBASE TRANSACTION ANALYSIS
============================================================
--- Input [0] ---
Prev TXID:    0000000000000000000000000000000000000000000000000000000000000000
Prev VOUT:    4294967295 (Coinbase identifier)
Script Length:77 bytes
Message:      The Times 03/Jan/2009 Chancellor on brink of second bailout for banks

--- Output [0] ---
Amount:       50.0 BTC
PK Script:    4104678afdb0fe5548271967f1a67130b7105cd6...

Locktime:     0

============================================================
                    VERIFICATION RESULTS
============================================================
Computed TXID:  4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b
Header Merkle:  4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b

[RESULT] SUCCESS: Transaction matches Merkle Root!
[RESULT] SUCCESS: Block Hash satisfies Difficulty!

```

---
### 03_nonce_diff.py

```
=================================================================
                   MINING & DIFFICULTY REPORT
=================================================================
nBits (Hex):      0x1d00ffff
Nonce (Decimal):  2083236893
Nonce (Hex):      0x7c2bac1d

Difficulty Target:
0x00000000ffff0000000000000000000000000000000000000000000000000000

Actual Block Hash:
0x000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
(000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f)
-----------------------------------------------------------------
STATUS: SUCCESS
The hash is LOWER than the target. Proof of Work is VALID.
-----------------------------------------------------------------
```

---
