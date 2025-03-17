# Lucioai assignment

- The base64 decoding was straight forward, I have used a small python script.

```python
import base64
encoded_message = "VGhpcyB3YXMgZWFzeS4gTGV0J3MgdHJ5IHNvbWV0aGluZyBoYXJkZXIuIE1yIENyeXB0byBuZWVkcyB5b3VyIGhlbHAgdG8gdW5kZXJzdGFuZCB0aGlzIHRleHQ6IAoKZ0FBQUFBQm5ibjhvTzBPN09tcXRxdWZjcDZOazVsNDQ4NEtwZ0xzNmFpaThLejJmX24yWFA2WmIzSUpmbXhPTzdpVHVfQXFZZWRPeTl3cEFLVk9ZNWttN3NxREpoVGR6dTJaQmxkbDgtdnd1bnJ2SGFMNjAyX1pPc09OLWtvRmJvOVNVZW13NHNjQm1JTkJFU1p0akJCUHljWUliNnV1WjZhV1E3MHl3bnNxWXJuOFp5cjVGYzJ1bVJrYUVnaFU1SlM4ZUt4VTlGQThLU1ptTWVxd2VDbFlNNG1tNEN5TzNuems3UEh3aHQ4dXNZU3BLbU5CclFjY1dDenZHQ3hGbDRUX1EwdFRKTWsxSklRX1dXaEpDY3hRTWVLTWxCSlYwb0UwQW9NZDRBd19vN0IzUWpURVFvckk9CgpIZSB0ZWxscyB5b3UgJ1NvbWV0aW1lcywgbWFjaGluZXMgaGF2ZSBuYW1lcyB0aGF0IGh1bWFucyBjYW4ndCByZWFkIHNvIHlvdSBuZWVkIGEgYm9vayB0byBsb29rIHVwIHRoZWlyIG5hbWVzLiBDaGVjayB0aGUgcHViJ3MgcmVjb3JkcyBpbiB0aGUgYm9vayBhbmQgeW91J2xsIGZpbmQgc29tZXRoaW5nIHRoYXQgbWlnaHQgYmUgdXNlZnVsLic="
decoded_message = base64.b64decode(encoded_message).decode('utf-8')
print(decoded_message)
```

- For the next one based on clues "Mr.Crypto" and the initial part of the second encoded string I was able to find it was an fernet cryptographic encryption and it needs a key to decode.
- For finding the key I have tried various things, Initially I thought that I would find something from the website (blogs and stuff) but it was not working
- Then while looking more into it, I got an idea to do a DNS lookup of the domain "lucioai.com", there I found the key in a TXT Record.
- I have used the website https://dnschecker.org for the lookup.
- Then I used a Small Python script to decode the second encryption.
```python
import base64
import binascii

import struct
import time
import six
_MAX_CLOCK_SKEW = 60

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.hmac import HMAC
from cryptography.fernet import Fernet

import sys

token = "gAAAAABWC9P7-9RsxTz_dwxh9-O2VUB7Ih8UCQL1_Zk4suxnkCvb26Ie4i8HSUJ4caHZuiNtjLl3qfmCv_fS3_VpjL7HxCz7_Q=="
key= ""

if (len(sys.argv)>1):
	token=sys.argv[1]

if (len(sys.argv)>2):
	key=sys.argv[2]

def decrypt(self, token, ttl=None):
  current_time = int(time.time())
  print("Current time:\t",time.ctime(current_time))

  print("\nToken Details")
  print("=============")
  if not isinstance(token, bytes):
    raise TypeError("token must be bytes.")




  try:
    data = base64.urlsafe_b64decode(token)
  except (TypeError, binascii.Error):
    print("error")

  print("Decoded data: ",binascii.hexlify(bytearray(data)))


f = Fernet(key)
decrypt(f,token.encode())
```
