import math
from collections import Counter

def shannon_entropy(data):
    """
    Calculate Shannon entropy for a given list of data.
    H(X) = -sum(p_i * log2(p_i)) for all unique values i
    """
    n = len(data)
    counts = Counter(data)
    entropy = 0
    for count in counts.values():
        p = count / n
        entropy -= p * math.log2(p)
    return entropy

# --- Example 1: Specific numbers ---
data1 = [3, 1, 2, 3, 2, 3]
entropy1 = shannon_entropy(data1)
print("1) Entropy for [3,1,2,3,2,3]:", entropy1)

# --- Example 2: Three dice rolls (6 sides each) ---
# Each die has 6 equally probable outcomes, 3 dice
num_sides = 6
entropy2 = 5 * math.log2(num_sides)  # 5 dice
print("2) Entropy for 5 dice rolls (6 sides):", entropy2)

# --- Example 3: Eight coin flips ---
# Each coin has 2 equally probable outcomes (heads/tails)
num_coins = 8
entropy3 = num_coins * math.log2(2)  # 1 bit per coin
print("3) Entropy for 8 coin flips:", entropy3)

"""
1) Entropy for [3,1,2,3,2,3]: 1.4591479170272446
2) Entropy for 5 dice rolls (6 sides): 12.92481250360578
3) Entropy for 8 coin flips: 8.0
"""
