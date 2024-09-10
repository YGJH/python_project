from pwn import *
import string
alphabet = string.ascii_lowercase+string.digits+'CTF{_}'
plain_flag = "picoCTF{bad_1d3a5_757157"
# plain_flag = ""
known1 = ['p' , 'i' , 'c' , 'o' , 'C' , 'T' , 'F' , '{' , 'b' , 'a' , 'd' , '_' , '1' , 'd' , '3' , 'a' ,'5','_','7','5','7','1','5','7']
known = []
# known = []
r = remote("mercury.picoctf.net" , 47987)
prompt = r.recvuntil('flag: ')
cipher_flag = r.recvline().strip().decode()
# print("Flag is: " + cipher_flag)
r.recvline()
r.recvline()
payload = plain_flag
r.sendafter("give me: " , payload+'\n')
prompt = r.recvuntil('Here you go: ')
cipher = r.recvline().strip().decode()

temp = ""
for chunk in known1:
    payload = temp+chunk
    r.sendafter("give me: " , payload+"\n")
    prompt = r.recvuntil("Here you go: ")
    cipher = r.recvline().strip().decode()
    for i in known:
        cipher = cipher.replace(i , '')
    temp+=chunk
    known.append(cipher)
    cipher_flag = cipher_flag.replace(cipher , '')
    print(known)






while '}' not in plain_flag:
    for c in alphabet:
        payload = plain_flag+c
        r.sendafter("give me: " , payload+"\n")
        prompt = r.recvuntil("Here you go: ")
        cipher = r.recvline().strip().decode()
        # print(plain_flag)
        for chunk in known:
            cipher = cipher.replace(chunk , '')
        if(cipher in cipher_flag):
            plain_flag += c
            cipher_flag = cipher_flag.replace(cipher , '')
            known.append(cipher)
            # print(f"cipher = {cipher}\nknown = {known}")
            print(plain_flag)
            break

print(f"plain_flag = {plain_flag}")
