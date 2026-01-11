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
