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
key= "-s6eI5hyNh8liH7Gq0urPC-vzPgNnxauKvRO4g03oYI="

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
