x = str(input())
n = int(input())
w = int(input())
pad = str(input())


# print(f"{' '*(w-len(x))}{x}")
# print(f"{n}{' '*(w-len(x))}")
# print(f"{pad*(((w-len(x))//2))}{x}{pad*((w-len(x))//2)}")
# le = (len(str(n))//3) - 1
# tmp = str(n)
# tmp = tmp[::-1]
# tmpp = ""
# count = 0
# for i in tmp:
#     if count == 3:
#         count=0
#         tmpp+=','
#     tmpp+=i
#     count+=1

# tmpp = tmpp[::-1]

# print(f"{pad*((w-len(tmpp))//2)}{tmpp}{pad*((w-(le+len(str(n))))//2)}")



print('{:>{wide}s}'.format(x ,wide=w))
print('{:<{wide}d}'.format(n ,wide=w))
print('{:{pad}^{wide}s}'.format(x ,wide=w,pad=pad))
print('{:{pad}^{wide},d}'.format(n ,wide=w,pad=pad))