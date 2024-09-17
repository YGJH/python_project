from Crypto.Util.number import *


p = q = getStrongPrime(1024)
while 1:
    q+=1
    if isPrime(q):
        break

flag = b'flag{asd7766zxc_is_a_gay}'
flag = bytes_to_long(flag)

n = p * q
phi = (p-1) * (q-1)


e = 65537
c = pow(flag , e , n)

d = inverse(e , phi)

assert(pow(c,d,n) == flag)

print(f"n = {n}")
print(f"e = {e}")
print(f"c = {c}")

m = pow(c ,d , n)
print(long_to_bytes(m))
