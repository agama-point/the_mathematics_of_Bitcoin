# the_Mathematics_of_Bitcoin

## 17) Mining

```
echo -n "AgamaPoint" | sha256sum

> 29b5a9c21f25fcc7c015fee558aa15dd28341487e76ac744583adb37eda1e2f7

```

We are searching for a nonce (an additional arbitrary number) for which the hash begins with the required number of leading zeros, meaning the hash is as short (low) as possible:

```
i=0; while ! (echo -n "Agama Point $i" | sha256sum | 
tr -d "\n"; echo " (nonce=$i)")|grep -E "^00"; 
do let i++; done

> 00999ac48b71fc267a67f78bb379d554020d062343d344269d62d4b9f55b90b1 - (nonce=263) 
```

---

```
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
```
