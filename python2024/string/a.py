x = input()
y = input()
z = input()
w = input()
if(y in x):
    print('True')
else:
    print('False')
if (x.find(y)):
    print(x.find(y))
else:
    print('-1')

a = x.split(',')
print(a)
count = 0
for i in a:
    print(i , end='')
    count+=1
    if(count != 3):
        print('---',end='')
    else:
        print()
        break


print(y in x[:len(y)])
print(y in x[-len(y):])
print(x.upper())


count = 0
st = ""
for i in x:
    if(i == ','):
        print(st,end='')
        print(',',end='')
        st=""
        continue
    elif i.isalpha():
        if st=="":
            st+=i.upper()
        else:
            st+=i
    else:
        st+=i

if st != "":
    print(st)
else:
    print()
print(y.isnumeric())
k = x.replace(y, z)
print(k)
w=w.strip()
print(w)
print(len(w))
