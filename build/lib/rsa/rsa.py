c = 62324783949134119159408816513334912534343517300880137691662780895409992760262021
n = 1280678415822214057864524798453297819181910621573945477544758171055968245116423923
e = 65537
p = 1899107986527483535344517113948531328331
q = 674357869540600933870145899564746495319033
# if(p*q == n):
#     print("yes")
# else:
#     print("no")
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

phi = (q-1)*(p-1)
# for i in range(1 ,10):
d = modinv(e , phi)
    # print(type(e))
    # print(d)
    # if(e*d % phi == 1):
    #     m = pow(c , d , n)
    #     print(f"m: {m}")

print(d)
# m = pow(c , d , n)
# print(bytearray.fromhex(hex(m)[2:]).decode())

# m = pow
# print()
    # hex_string = hex(m)[2:]
    # print(f"hex:{hex_string}")
    # byte_array = bytes.fromhex(hex_string)
    # print(byte_array.decode('ascii'))
