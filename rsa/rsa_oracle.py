password = 873224563026311790736191809393138825971072101706285228102516279725246082824238887755080848591049817640245481028953722926586046994669540835757705139131212
from pwn import *
from Crypto.Util.number import *
r = remote("titan.picoctf.net" , 54522)


response = r.recvuntil('decrypt.')
print(response.decode())
payload = b'E' + b'\n'
r.send(payload)
reponse = r.recvuntil('keysize): ')
payload = b'\x02'+b'\n'
r.send(payload)
r.recvuntil('ciphertext (m ^ e mod n) ')
ci = r.recvline()
reponse = r.recvuntil('decrypt.')



ke = int(ci.decode())
pa = password * ke
r.send(b'D'+b'\n')
r.recvuntil('decrypt: ')
print(f"str(pa) = {str(pa)}")
r.send(str(pa) + '\n')
response = r.recvuntil("(c ^ d mod n): ")
print(response.decode())
ans = r.recvline()
print(f"ans = {ans.decode()}")


ans = int(ans , 16)
ans = ans // 2
ans = long_to_bytes(ans)
ans = ans.decode()
print(f"ans = {ans}")
os.system("openssl enc -aes-256-cbc -d -in ./cipher/secret.enc -k " + ans)