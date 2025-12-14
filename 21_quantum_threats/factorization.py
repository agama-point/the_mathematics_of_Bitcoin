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
    N0 =      261_980_999_226_229 # 2 s
    N1 =    1_125_897_758_834_689
    N = 6_380_635_780_987_411_231 # 2147483647 * 2971215073 
    print(f"N = {N}")

    start = time.time()
    factors = factorize(N)
    elapsed = time.time() - start

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


# M19 * M31 = 1125897758834689
N = 1125897758834689
Prime factors:
524287
2147483647
Factorization time: 0.098830 s

# M31 * M67
NX  = 316_912_649_909_483_397_782_351_904_769 # 2147483647 * 147573952589676412927

NX2 = 259_025_452_848_852_042_527 # 87178291199 * 2971215073
"""

"""
factorial:  
2, 3, 5, 7, 23, 719, 5039, 39916801, 479001599, 87178291199, 10888869450418352160768000001

fibonacci:
2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437, 2971215073, 99194853094755497
"""
