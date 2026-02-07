def fermat_inv(n, p):
    inverse = pow(n, p-2, p)
    # print(f'Inverting {n} modulo {p} -> {inverse}')
    temp_fi = n ** (p-2)
    return temp_fi, inverse


# iWarp inspir:
def inverses_mod_n(n):
    print(f"\nMultiplicative inverses modulo {n}:")
    info_mod = "mod "+str(n)+" →"
    for a in range(n):
        inverse = None
        for b in range(n):
            if (a * b) % n == 1:
                inverse = b
                break

        if inverse is None:
            print(f"{a:>2} → no inverse / ", a,"*",b,"=",a*b, info_mod,a*b % n )
        else:
            dt, dfi = fermat_inv(a,n) 
            ds = "f: " + str(dt)+" % " + str(dt%n) + "==" + str(dfi)
            print(f"{a:>2} → inverse is {inverse} /", a,"*",b,"=",a*b, info_mod, a*b % n,ds)


def analyze_mod_n(n):
    inverses_mod_n(n)


# ===========================================================
print("-"*30)

analyze_mod_n(4)
analyze_mod_n(5)
analyze_mod_n(6)
analyze_mod_n(7)
analyze_mod_n(12)
analyze_mod_n(13)

"""
---------------------------------------------------
Multiplicative inverses modulo 4:
 0 → no inverse /  0 * 3 = 0 mod 4 → 0
 1 → inverse is 1 / 1 * 1 = 1 mod 4 → 1 f: 1 % 1==1
 2 → no inverse /  2 * 3 = 6 mod 4 → 2
 3 → inverse is 3 / 3 * 3 = 9 mod 4 → 1 f: 9 % 1==1

Multiplicative inverses modulo 5:
 0 → no inverse /  0 * 4 = 0 mod 5 → 0
 1 → inverse is 1 / 1 * 1 = 1 mod 5 → 1 f: 1 % 1==1
 2 → inverse is 3 / 2 * 3 = 6 mod 5 → 1 f: 8 % 3==3
 3 → inverse is 2 / 3 * 2 = 6 mod 5 → 1 f: 27 % 2==2
 4 → inverse is 4 / 4 * 4 = 16 mod 5 → 1 f: 64 % 4==4

Multiplicative inverses modulo 6:
 0 → no inverse /  0 * 5 = 0 mod 6 → 0
 1 → inverse is 1 / 1 * 1 = 1 mod 6 → 1 f: 1 % 1==1
 2 → no inverse /  2 * 5 = 10 mod 6 → 4
 3 → no inverse /  3 * 5 = 15 mod 6 → 3
 4 → no inverse /  4 * 5 = 20 mod 6 → 2
 5 → inverse is 5 / 5 * 5 = 25 mod 6 → 1 f: 625 % 1==1

Multiplicative inverses modulo 7:
 0 → no inverse /  0 * 6 = 0 mod 7 → 0
 1 → inverse is 1 / 1 * 1 = 1 mod 7 → 1 f: 1 % 1==1
 2 → inverse is 4 / 2 * 4 = 8 mod 7 → 1 f: 32 % 4==4
 3 → inverse is 5 / 3 * 5 = 15 mod 7 → 1 f: 243 % 5==5
 4 → inverse is 2 / 4 * 2 = 8 mod 7 → 1 f: 1024 % 2==2
 5 → inverse is 3 / 5 * 3 = 15 mod 7 → 1 f: 3125 % 3==3
 6 → inverse is 6 / 6 * 6 = 36 mod 7 → 1 f: 7776 % 6==6

Multiplicative inverses modulo 12:
 0 → no inverse /  0 * 11 = 0 mod 12 → 0
 1 → inverse is 1 / 1 * 1 = 1 mod 12 → 1 f: 1 % 1==1
 2 → no inverse /  2 * 11 = 22 mod 12 → 10
 3 → no inverse /  3 * 11 = 33 mod 12 → 9
 4 → no inverse /  4 * 11 = 44 mod 12 → 8
 5 → inverse is 5 / 5 * 5 = 25 mod 12 → 1 f: 9765625 % 1==1
 6 → no inverse /  6 * 11 = 66 mod 12 → 6
 7 → inverse is 7 / 7 * 7 = 49 mod 12 → 1 f: 282475249 % 1==1
 8 → no inverse /  8 * 11 = 88 mod 12 → 4
 9 → no inverse /  9 * 11 = 99 mod 12 → 3
10 → no inverse /  10 * 11 = 110 mod 12 → 2
11 → inverse is 11 / 11 * 11 = 121 mod 12 → 1 f: 25937424601 % 1==1

Multiplicative inverses modulo 13:
 0 → no inverse /  0 * 12 = 0 mod 13 → 0
 1 → inverse is 1 / 1 * 1 = 1 mod 13 → 1 f: 1 % 1==1
 2 → inverse is 7 / 2 * 7 = 14 mod 13 → 1 f: 2048 % 7==7
 3 → inverse is 9 / 3 * 9 = 27 mod 13 → 1 f: 177147 % 9==9
 4 → inverse is 10 / 4 * 10 = 40 mod 13 → 1 f: 4194304 % 10==10
 5 → inverse is 8 / 5 * 8 = 40 mod 13 → 1 f: 48828125 % 8==8
 6 → inverse is 11 / 6 * 11 = 66 mod 13 → 1 f: 362797056 % 11==11
 7 → inverse is 2 / 7 * 2 = 14 mod 13 → 1 f: 1977326743 % 2==2
 8 → inverse is 5 / 8 * 5 = 40 mod 13 → 1 f: 8589934592 % 5==5
 9 → inverse is 3 / 9 * 3 = 27 mod 13 → 1 f: 31381059609 % 3==3
10 → inverse is 4 / 10 * 4 = 40 mod 13 → 1 f: 100000000000 % 4==4
11 → inverse is 6 / 11 * 6 = 66 mod 13 → 1 f: 285311670611 % 6==6
12 → inverse is 12 / 12 * 12 = 144 mod 13 → 1 f: 743008370688 % 12==12
"""