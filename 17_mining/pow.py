import hashlib
import time

def mine_with_prefix(prefix, min_zeros, max_iterations=1_000_000):
    nonce = 0
    start_time = time.time()
    found_count = 0
    
    print(f"Starting mining with prefix: '{prefix}'")
    print(f"Target: Minimum {min_zeros} leading zeros")
    print(f"Limit:  {max_iterations:,} iterations")
    print("-" * 70)
    print(f"{'Time':<6} | {'Zeros':<5} | {'Full Str. (Prefix + Nonce)':<25} | {'Hash'}")
    print("-" * 70)

    try:
        while nonce < max_iterations:
            # Combine prefix, space, and nonce
            input_str = f"{prefix} {nonce}"
            content = input_str.encode()
            hash_result = hashlib.sha256(content).hexdigest()

            # Count leading zeros
            current_zeros = 0
            for char in hash_result:
                if char == '0':
                    current_zeros += 1
                else:
                    break

            # If it meets the requirement, print it
            if current_zeros >= min_zeros:
                elapsed = time.time() - start_time
                m, s = divmod(int(elapsed), 60)
                time_str = f"{m:02d}:{s:02d}"
                
                print(f"{time_str:<6} | {current_zeros:<5} | {input_str:<25} | {hash_result}")
                found_count += 1

            nonce += 1
            
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")

    total_time = time.time() - start_time
    # Avoid division by zero if interrupted immediately
    hps = nonce / total_time if total_time > 0 else 0
    
    print("-" * 70)
    print(f"Mining finished in {total_time:.2f} seconds.")
    print(f"Total nonces checked: {nonce:,}")
    print(f"Performance: {hps:,.0f} hashes/second")
    print(f"Total matches found: {found_count}")

if __name__ == "__main__":
    # USER INPUTS
    SEARCH_TEXT = "Agama Point"
    REQUIRED_ZEROS = 6
    LIMIT = 1_000_000_000 
    
    mine_with_prefix(prefix=SEARCH_TEXT, min_zeros=REQUIRED_ZEROS, max_iterations=LIMIT)

"""
Starting mining with prefix: 'Agama Point'
Target: Minimum 6 leading zeros
Limit:  1,000,000,000 iterations
----------------------------------------------------------------------
Time   | Zeros | Full Str. (Prefix + Nonce) | Hash
----------------------------------------------------------------------
00:01  | 6     | Agama Point 587451        | 0000007f91c02305905d3583c461bb1985b8f957524b115a0287ab5bd0901f00     
00:03  | 6     | Agama Point 2123272       | 000000b910326dd7aba40635a41e6bf46b99c90345571102d962741ba4b74e7a     
00:32  | 6     | Agama Point 18631304      | 000000fb40d8cdbcb133d71bac3c3834eba04b20d41508bfdbaccb8feda8b24d
01:53  | 6     | Agama Point 67641080      | 000000bddcfdf8a1c4c116cb568ab00d74034c99da9550ccd9a4c0faf501eb89
03:28  | 6     | Agama Point 124777002     | 00000022a2266f5aee910cbf9769a264eebd0e6645a497fa02a95786f100d5f3
04:26  | 6     | Agama Point 159567104     | 00000033e63ddcd961d38edd4df898c47a9af13e95aee7aae84e2014a2dec5fc
04:30  | 6     | Agama Point 162220439     | 0000009807c8cc49f76c31e49e9bf8589533f35d728e06975c01ca92c7e74c14
04:41  | 6     | Agama Point 168431369     | 000000292892702def296d0ac8a6c3f037ff629c61d68a2f2d4c78750dddc617
05:27  | 6     | Agama Point 195999718     | 000000b8d5eb0c149f9444e58f146a1efc523a8103bdb235b26a0507545d9a9a
05:50  | 7     | Agama Point 209949850     | 00000005434496a4937f988f644002737b4cda57137fd05f061690de6ca715a5
06:10  | 6     | Agama Point 222198260     | 000000f578899499d5e3624a3f10bd1aed03f4bec487a21345111a62d964e0e9
...
"""