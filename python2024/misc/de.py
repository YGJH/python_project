# from decimal import *
# import decimal as dc

def C(m , n):
    a = m
    ret = 1
    if n > m/2:
        n = m - n
    for i in range(1 , n+1):
        ret *= a
        ret /= i
        a-=1
    return ret

m = int(input())
n = int(input())
print(int(C(m , n)))


# def fac(n):
#     if n==0:
#         return 1
#     else:
#         return n * fac(n-1)

# n = int(input())
# m = int(input())
# print(int(fac(n)/fac(m)*fac(n-m)))
