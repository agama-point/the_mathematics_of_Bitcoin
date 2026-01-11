# the_Mathematics_of_Bitcoin

## 17) Mining

```
echo -n "AgamaPoint" | sha256sum

```

We are searching for a nonce (an additional arbitrary number) for which the hash begins with the required number of leading zeros, meaning the hash is as short (low) as possible:

```
i=0; while ! (echo -n "Agama Point $i" | sha256sum | 
tr -d "\n"; echo " (nonce=$i)")|grep -E "^00"; 
do let i++; done
```
