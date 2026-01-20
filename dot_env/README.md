## Using `.env` (environment variables) in Python

### What is .env used for?

The .env file is used to store sensitive or configuration data such as API keys, secrets, or tokens:

- keeps private data out of source code,

- prevents committing secrets to Git,

- allows different configuration per environment (dev / prod).



### Install required library
To work with a `.env` file in Python, install **python-dotenv**:

```bash
pip install python-dotenv
```


### Best practice

Add .env to .gitignore to avoid leaking secrets:
```
.env
```

---

### Use it in Python

Example of loading and using two environment variables:



.env

```
KEY1=abc123
KEY2=secret456
```




```python
from dotenv import load_dotenv
import os

load_dotenv()  # loads variables from .env

key1 = os.getenv("KEY1")
key2 = os.getenv("KEY2")

print(key1)
print(key2)
```



