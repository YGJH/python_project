import sys
# ev = []
# od = []
evv = 0
odd = 0
for line in sys.stdin:
    now = line.split(' ')    
    for x in now:
        if int(x)%2==1:
            # od.ppend(x)
            odd+=int(x)
        else:
            # ev.append(x)
            evv+=int(x)

print('odd:{} even:{}'.format(odd,evv))

