s = input()
exec(f"dic = {s}" , globals() , locals())

s = list(dic)
print(len(s))

x = input()
try:
    print(dic[x])
except Exception:
    print("False")
x = int(input())

if x in dic:
    print(dic[x]==0)
else:
    print("Notexisting")


tup = input()
exec(f"tup = {tup}" , globals() , locals())
dic[tup[0]] = tup[1]

s = list(dic.keys())

s = list(sorted(s))
for i in s:
    print(i)


s = list(dic.values())

s = list(sorted(s))
for i in s:
    print(i)
s = list(dic.items())
s = list(sorted(s))
for i in s:
    print(i)


sor = input()
exec(f"sor = {sor}")

sorKey = list(sor)
print(len(sorKey))
x = int(input())
print(x in sorKey)
y=input()
if y in sor:
    if sor[y]==0:
        print("True")
    else:
        print("False")
else:
    print("Notexisting")

tup = input()
exec(f"tup = {tup}")
sor[tup[0]] = tup[1]
for key in sorted(sor.keys()):
    print(key)
for values in sorted(sor.values()):
    print(values)
for key in sorted(sor.keys()):
    print(f"({key}, {sor[key]})")
