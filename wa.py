import math as ma

x = int(input())

answer = "list1 = [(i , j , int(ma.sqrt(i * i + j * j))) for i in range(1 , x+1) for j in range(i , x+1) if ma.sqrt((i*i)+(j*j))==int(ma.sqrt((i*i)+(j*j))) and ma.sqrt(i*i+j*j) <= x]"

exec(answer , globals() , locals())
print(list1)