import itertools

x = int(input())

answer = "list2 = [(i, j, k) for i in range(1, x+1, 1) for j in range(i+1, x+1, 1) for k in range(j+1, x+1, 1) if (i**2+j**2)==k**2]"

_cmd ='' 
while True:
    try:
        _s = input()
        _cmd += _s+'\n'
    except EOFError:
        break

p = compile(_cmd,'default','exec')
exec(p)

exec(answer , globals() , locals())
print(list2)