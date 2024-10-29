list1 = list(map(int,input().split(',')))

# print(list1)
j = 0
e = len(list1)
for i in list1:
    print(f"{j}:{i}", end='')
    j+=1
    if j < e:
        print(',', end='')
    else:
        break

print()
list2=[num for num in list1 if num>0]
# print(f"list2 = {list2}")
list1 = [num for num in list1 if num < 0]

e = min(len(list1) , len(list2))
# print(f"e = {e}")
P = 1
for i,j in zip(list2 , list1):
    print(f"{i}:{j}", end='')
    if(P < e):
        print(',',end='')
    P+=1
print()