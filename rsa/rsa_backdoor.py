from Crypto.Util.number import *
import binascii

# ed % phi = 1
# ed = 1 + k*phi
# c ^ backdoor = (m^e) ^ (d^2*e + 7phi) = m^(e*d*d*e + e * 7phi) = m ^ ((phi-1) * (phi-1) + 7ephi) = m ^ 1

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
    

# encrypt
flag = "flag{asd_is_gay}"
bytearray_flag = flag.encode()
hex_array = binascii.hexlify(bytearray_flag)
# print(hex_array)
m = int(hex_array , 16)
print(m)
def get_key():
    p = getPrime(1024)
    q = getPrime(1024)
    phi = (p-1) * (q-1)
    n = p * q
    e = getPrime(1024)
    d = modinv(e , phi)
    return n , e , d , phi
n , e, d, phi = get_key()

while e*d % phi != 1:
    n , e, d, phi = get_key()

c = pow(m , e , n)
hint = pow(d,2)*e + 7*phi
print(f"n = {n}")
print(f"e = {e}")
print(f"c = {c}")
print(f"d^2*e + 7phi = {hint}")

# decrypty
ans = pow(c , hint , n)
hex_ans = hex(ans)[2:]
byte_ans = bytes.fromhex(hex_ans)
print(f"ans = {byte_ans.decode('ascii')}")

