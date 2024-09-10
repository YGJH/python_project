
def fac(p):
    if p==0:
        return 1
    else:
        return p * fac(p-1)

n = int(input())
m = int(input())
a = fac(n)
b = fac(m)
c = fac(n-m)
print(a)
print(b)
print(c)

print(int(fac(n)/fac(m)*fac(n-m)))
# print(m)