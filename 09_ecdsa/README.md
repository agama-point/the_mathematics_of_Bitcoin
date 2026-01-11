# the_Mathematics_of_Bitcoin

## 09) ECC | ECDSA | Secp256k1

---

### secp256k1 Curve Point Verification

point.py: This small script verifies that the generator point **G** lies on the **secp256k1** elliptic curve used by Bitcoin.

The curve equation is:

y² ≡ x³ + 7 (mod p)

The program substitutes the official generator coordinates **Gx** and **Gy** into the equation and checks that both sides are equal modulo the prime field **p**.  
If the computed difference is zero, the point is valid and lies on the curve.

This is the fundamental validation step used in elliptic curve cryptography to ensure that a point is mathematically valid.


```python
# secp256k1 parameters
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F

Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
```

```
y^2 mod p = 32748224938747404814623910738487752935528512903530129802856995983256684603122
x^3 + 7 mod p = 32748224938747404814623910738487752935528512903530129802856995983256684603122
difference = 0
```

---

