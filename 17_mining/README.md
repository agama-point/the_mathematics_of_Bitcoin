# the_Mathematics_of_Bitcoin

## 17) Mining

```
echo -n "AgamaPoint" | sha256sum

```
---

```
i=0; while ! (echo -n "Agama Point $i" | sha256sum | 
tr -d "\n"; echo " (nonce=$i)")|grep -E "^00"; 
do let i++; done
```
