# ------------------------------------------------------
# ECC Point Doubling Example
# Curve: y^2 = x^3 + 7 mod 17
# Point: G = (x1, y1)
# ------------------------------------------------------

# Initial point
x1, y1 = 15, 13
p = 17  # Prime modulus for the finite field

# Function to calculate multiplicative inverse modulo p
def inv(n, p):
    """
    Returns the multiplicative inverse of n modulo p.
    Using Fermat's little theorem (works for prime p):
        n^-1 ≡ n^(p-2) mod p
    """
    inverse = pow(n, p-2, p)
    print(f"Inverting {n} modulo {p} → {inverse}")
    return inverse

print(f"Starting point G = ({x1}, {y1}) on curve y^2 = x^3 + 7 mod {p}\n")

# Step 1: Compute the slope lambda = (3*x1^2) / (2*y1) mod p
numerator = 3 * x1**2
denominator = 2 * y1
print(f"Step 1: Compute slope λ numerator = 3*x1^2 = {numerator}")
print(f"Step 1: Compute slope λ denominator = 2*y1 = {denominator}")

denominator_inv = inv(denominator, p)  # multiplicative inverse of denominator modulo p
lambda_ = (numerator * denominator_inv) % p
print(f"Step 1: Slope λ = (numerator * denominator_inv) % p = {lambda_}\n")

# Step 2: Compute new x-coordinate: x2 = λ^2 - 2*x1 mod p
x2 = (lambda_**2 - 2*x1) % p
print(f"Step 2: Compute x2 = (λ^2 - 2*x1) % p = ({lambda_}^2 - 2*{x1}) % {p} = {x2}")

# Step 3: Compute new y-coordinate: y2 = λ*(x1 - x2) - y1 mod p
y2 = (lambda_ * (x1 - x2) - y1) % p
print(f"Step 3: Compute y2 = (λ*(x1 - x2) - y1) % p = ({lambda_}*({x1}-{x2}) - {y1}) % {p} = {y2}\n")

print(f"Result: 2G = ({x2}, {y2})")


"""
Step 1: Compute slope λ numerator = 3*x1^2 = 675
Step 1: Compute slope λ denominator = 2*y1 = 26
Inverting 26 modulo 17 → 2
Step 1: Slope λ = (numerator * denominator_inv) % p = 7

Step 2: Compute x2 = (λ^2 - 2*x1) % p = (7^2 - 2*15) % 17 = 2
Step 3: Compute y2 = (λ*(x1 - x2) - y1) % p = (7*(15-2) - 13) % 17 = 10

Result: 2G = (2, 10)
"""