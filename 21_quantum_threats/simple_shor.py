import math
import random


def find_period(a, N):
    """
    Find the period r of the function f(x) = a^x mod N.
    This simulates the information obtained from the Quantum Fourier Transform.
    """
    print("\n  [Period finding]")
    print(f"  Evaluating powers of a = {a} modulo N = {N}")

    value = 1
    for r in range(1, N + 1):
        value = (value * a) % N
        print(f"    a^{r} mod {N} = {value}")

        if value == 1:
            print(f"  ➜ Period detected: r = {r}")
            return r

    print("  ✖ Period not found")
    return None


def shor_simulation(N, max_attempts=10):
    """
    Classical, step-by-step simulation of Shor's algorithm with verbose output.
    """
    print("\n============================================")
    print("      SHOR'S ALGORITHM – SIMULATION")
    print("============================================\n")

    print(f"Target number to factor: N = {N}")

    # Quick classical shortcut
    if N % 2 == 0:
        print("N is even. Trivial factorization.")
        return 2, N // 2

    for attempt in range(1, max_attempts + 1):
        print("\n--------------------------------------------")
        print(f"Attempt {attempt}")
        print("--------------------------------------------")

        # Step 1: Choose random a
        a = random.randrange(2, N)
        print(f"Chosen random base a = {a}")

        # Step 2: Compute gcd(a, N)
        g = math.gcd(a, N)
        print(f"gcd({a}, {N}) = {g}")

        if g != 1:
            print("✔ Non-trivial divisor found immediately.")
            print(f"Factorization: {N} = {g} × {N // g}")
            return g, N // g

        print("a and N are coprime. Proceeding to quantum subroutine.")

        # Step 3: Period finding (QFT result simulation)
        r = find_period(a, N)

        if r is None:
            print("✖ Failed to determine period. Trying new a.")
            continue

        # Step 4: Check parity of r
        if r % 2 != 0:
            print("✖ Period is odd. This run cannot succeed.")
            continue

        print(f"Period r = {r} is even. Continuing.")

        # Step 5: Compute a^(r/2) mod N
        x = pow(a, r // 2, N)
        print(f"a^(r/2) mod N = a^{r//2} mod {N} = {x}")

        if x == 1 or x == N - 1:
            print("✖ Trivial result (±1 mod N).")
            continue

        # Step 6: Compute candidate factors
        p = math.gcd(x - 1, N)
        q = math.gcd(x + 1, N)

        print(f"gcd({x} - 1, {N}) = {p}")
        print(f"gcd({x} + 1, {N}) = {q}")

        # Step 7: Validate factors
        if p > 1 and q > 1 and p * q == N:
            print("\n🎉 SUCCESS")
            print(f"Non-trivial factorization found:")
            print(f"{N} = {p} × {q}")
            return p, q

        print("✖ Factors invalid. Trying another attempt.")

    print("\n❌ Failed to factor N within attempt limit.")
    return None


# --------------------------------------------------
# MAIN EXECUTION
# --------------------------------------------------
if __name__ == "__main__":
    # Change N here to test different numbers (e.g. 15, 21, 33)
    # N = 15
    N = 21

    result = shor_simulation(N)

    if result:
        p, q = result
        print("\nFinal result:")
        print(f"{N} = {p} × {q}")
    else:
        print("\nNo factorization found.")

"""
============================================
      SHOR'S ALGORITHM – SIMULATION
============================================

Target number to factor: N = 21

--------------------------------------------
Attempt 1
--------------------------------------------
Chosen random base a = 11
gcd(11, 21) = 1
a and N are coprime. Proceeding to quantum subroutine.

  [Period finding]
  Evaluating powers of a = 11 modulo N = 21
    a^1 mod 21 = 11
    a^2 mod 21 = 16
    a^3 mod 21 = 8
    a^4 mod 21 = 4
    a^5 mod 21 = 2
    a^6 mod 21 = 1
  ➜ Period detected: r = 6
Period r = 6 is even. Continuing.
a^(r/2) mod N = a^3 mod 21 = 8
gcd(8 - 1, 21) = 7
gcd(8 + 1, 21) = 3

🎉 SUCCESS
Non-trivial factorization found:
21 = 7 × 3

Final result:
21 = 7 × 3
"""