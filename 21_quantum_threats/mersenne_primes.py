exponents = [2, 3, 5, 7, 13, 17, 19, 31, 67, 127, 257]

def mersenne(p: int) -> int:
    return (1 << p) - 1   # efektivní zápis 2**p - 1

for p in exponents:
    m = mersenne(p)
    print(f"p = {p:3d} -> M_p = 2^{p} - 1 = {m}")

