import binascii
from Crypto.Util.number import *
def egcd(a, b):
    if a==0:
        return (b,0,1)
    else:
        g, x, y = egcd(b % a , a)
        return (g, y-(b//a) * x , x)
def modinv(b, n):
    g, x, _ = egcd(b , n)
    if g==1:
        return x % n
st = "Hello World"

def get_key():
    p = getPrime(100)
    q = getStrongPrime(1024 , p)
    phi = (p-1) * (q-1)
    e = getStrongPrime(1024 , p*q)
    d = modinv(e , phi)
    n = p * q
    return phi , n , e, d

phi , n , e , d = get_key()
assert(e*d % phi == 1)

st = st.encode()
# print(st)
res = binascii.hexlify(bytearray(st))
# print(res)
m = int(res, 16)
c = pow(m , e , n)
print(f"加密後: {c}")
ans = pow(c , d , n)

print((bytes.fromhex(hex(ans)[2:])).decode('ascii'))