import decimal as dc
# from decimal import *
# dc.getcontext().prec = 20
m = dc.Decimal(input())
r = dc.Decimal(input())
y = dc.Decimal(input())
# ans = dc.Decimal(m*(1+r)) ** dc.Decimal(y)
ans = m*(1+r) ** y

print(f"本金:{m}")

print(f"利率:{r}")
print(f"存幾年:{y}")
print(f"本利和:{ans}")