# -*- coding: utf-8 -*-

### BASE64
import base64

s = 'base64 encode'
encoded = base64.b64encode(s.encode('utf-8'))
print(encoded) # b'YmFzZTY0IGVuY29kZQ=='

decoded = base64.b64decode(encoded)
print(decoded) # b'base64 encode'


### URLエンコーディング
import urllib.parse
u = urllib.parse.urlencode({'a': "goto's", 'b': '?foo バー'})
print(u)

### MD5
import hashlib

h = hashlib.md5(b"Nobody inspects the spammish repetition").hexdigest() # 128bits
print(h) # bb649c83dd1ea5c9d9dec9a18df0ffe9

### SHA-1
import hashlib

h = hashlib.sha1(b"Nobody inspects the spammish repetition").hexdigest() # 160bits
print(h) # 531b07a0f5b66477a21742d2827176264f4bbfe2

### SHA-2
import hashlib

h = hashlib.sha224(b"Nobody inspects the spammish repetition").hexdigest() # 224bits
print(h) # a4337bc45a8fc544c03f52dc550cd6e1e87021bc896588bd79e901e2

h = hashlib.sha256(b"Nobody inspects the spammish repetition").hexdigest() # 256bits
print(h) # 031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406


