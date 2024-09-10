# from pwn import *

# connection = remote('titan picoctf.net', '50547')

# response = connection.recvuntil('decrypy.')
# print(response.decode())
# payload = b'E' + b'\n'

# connection.send(payload)

# response = connection.recvuntil('keysize):')
# print(response.decode())

# payload = b'\x02' + b'\n'
# connection.send(payload)
# response = connection.recvuntil('ciphertext (m ^ e mod n)')
# response = connection.recvline

text2 = 4707619883686427763240856106433203231481313994680729548861877810439954027216515481620077982254465432294427487895036699854948548980054737181231034760249505
text = 873224563026311790736191809393138825971072101706285228102516279725246082824238887755080848591049817640245481028953722926586046994669540835757705139131212

num = text2*text
# print(num)
# ans = '2bd79263f6'
ans = 'b2bd79263f6'
# print(ans)
# ans = 'c8c2607272'
num = int(ans , 16)//2
print(num)
hex_string = hex(num)
# hex_string = '0595ebc931fb'
print(hex_string)
byte_array = bytes.fromhex(hex_string)
print(byte_array)
print(ans.decode('ascii'))



# from pwn import *

# connection = remote('titan.picoctf.net', 55983)

# # Get the first messages and send encrypt
# response = connection.recvuntil('decrypt.')
# print(response.decode())
# payload = b'E' + b'\n'

# connection.send(payload)

# response = connection.recvuntil('keysize):')
# print(response.decode())

# # We want to encrypt the number 2
# payload = b'\x02' + b'\n'
# connection.send(payload)
# response = connection.recvuntil('ciphertext (m ^ e mod n)')
# response = connection.recvline()

# # We now have 2^e, we want to multiply by m^e (from the file password.enc)
# num=int(response.decode())*873224563026311790736191809393138825971072101706285228102516279725246082824238887755080848591049817640245481028953722926586046994669540835757705139131212

# # We now choose to decrypt
# response = connection.recvuntil('decrypt.')
# print(response.decode())
# payload = b'D' + b'\n'
# connection.send(payload)

# # We decrypt 2^e*m^e, which will yield 2*m
# response = connection.recvuntil('decrypt:')
# print(response.decode())
# connection.send(str(num)+'\n')

# response = connection.recvuntil('hex (c ^ d mod n):')
# print(response.decode())
# response = connection.recvline()
# print(response.decode())

# # we grab the response, convert it from hexadecimal and divide by 2
# num=int(response,16)//2
# print(hex(num))

# # Now we convert this to ASCII
# hex_string=hex(num)[2:] # get rid of 0x
# byte_array=bytes.fromhex(hex_string)
# print(byte_array.decode('ascii'))

# # Close the connection
# connection.close()
