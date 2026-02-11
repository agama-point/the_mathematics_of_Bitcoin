import math

def frac_sqrt_bytes_of_primes(count=7):
    primes = []
    n = 2
    while len(primes) < count:
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.append(n)
        n += 1

    iv = []
    for p in primes:
        frac = math.sqrt(p) % 1
        iv.append(int(frac * 256))

    return iv, primes


iv, primes = frac_sqrt_bytes_of_primes(7)

for p, v in zip(primes, iv):
    print(f"prime {p:2d}: 0x{v:02x}  {v:08b}")