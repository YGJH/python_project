from itertools import *
c = input()
# print(c)
# dic = dict()

ap = [chr(ch) for ch in range(65 , 91)]
ap = ap[:(ord(c)-64)]


answer = "{frozenset(num):len(num) for i in range(1 , len(ap)+1) for num in combinations(ap , i)}"
# print(dic)
