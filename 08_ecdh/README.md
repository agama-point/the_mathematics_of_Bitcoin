# the_mathematics_of_Bitcoin

## 08) ECCDH


### Simplified Elliptic Curve Demo (Field modulo 17)

This example uses a very small finite field **mod 17** to demonstrate how elliptic-curve arithmetic works without large numbers.  
The curve is defined in the form:

y² = x³ + ax + b (mod 17)


Because the field is tiny, every point on the curve can be printed, making the behavior easy to visualize.  
The script shows:

- how to evaluate the curve equation modulo 17  
- how to list all valid points `(x, y)` that satisfy the equation  
- how point addition and doubling work step by step  
- how scalar multiplication `k * G` emerges from repeated additions

This small-scale model behaves exactly like real elliptic curves used in cryptography, only with toy-sized numbers.  
It is ideal for learning and for understanding the underlying mathematics before moving to real curves such as **secp256k1**.  



```
--- Scalar multiplication by repeated adding ---
1 . (15, 13)
2 . (2, 10) *
3 . (8, 3)
4 . (12, 1)
5 . (6, 6)
6 . (5, 8)
7 . (10, 15)
8 . (1, 12) **
9 . (3, 0)
10 . (1, 5) ***
11 . (10, 2)
12 . (5, 9)
13 . (6, 11)
14 . (12, 16)
15 . (8, 14)
16 . (2, 7)
17 . (15, 4)
========================================
Verification test: 8G + 2G = 10G
8G + 2G = (1, 5)
* + ** = ***

```




---


### Simple Elliptic Curve Example (Bitcoin secp256k1)

This example demonstrates the minimal code needed to work with an elliptic curve over a finite field, using the Bitcoin curve **secp256k1**.  
The script defines the curve parameters, a base point `G`, and shows how to perform **scalar multiplication** on the curve.

It illustrates:

- definition of an elliptic curve of the form `y² = x³ + ax + b (mod p)`
- a simple point class with addition and doubling
- scalar multiplication using the double-and-add method
- computing `k * G` to obtain a public key point

The goal of this example is to provide a clean and minimal demonstration of how elliptic-curve arithmetic works at its core, without external libraries.  
This is useful for educational purposes and for understanding the foundations of Bitcoin’s cryptography.


--
