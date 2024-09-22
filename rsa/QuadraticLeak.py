from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes, bytes_to_long

flag = b'flag{society_call_you_gay}'
flag = bytes_to_long(flag)
key = RSA.generate(4096)
n = key.n
e = key.e
p, q = key.p, key.q

leak = (p**2 + q**2 - p - q)%key.n

ciph = pow(flag, key.e, key.n)

print(f'n = {n}')
print(f'e = {e}')
print(f'leak = {leak}')
print(f'ciph = {long_to_bytes(ciph)}')