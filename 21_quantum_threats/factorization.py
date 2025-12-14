import time
import math
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1 if d == 2 else 2  # 
    if n > 1:
        factors.append(n)
    return factors


if __name__ == "__main__":
    N = 261_980_999_226_229

    start = time.time()
    factors = factorize(N)
    elapsed = time.time() - start

    print(f"N = {N}")
    print("Prime factors:")
    for p in factors:
        print(p)
    print(f"Factorization time: {elapsed:.6f} s")

"""
N = 261980999226229
Prime factors:
15538213
16860433
Factorization time: 2.635 s
"""
