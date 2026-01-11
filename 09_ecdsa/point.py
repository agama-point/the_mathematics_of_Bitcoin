# secp256k1 parameters
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F

Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8

# left and right side of the curve equation
left = (Gy * Gy) % p
right = (pow(Gx, 3, p) + 7) % p

print("y^2 mod p =", left)
print("x^3 + 7 mod p =", right)
print("difference =", (left - right) % p)