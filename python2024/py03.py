strr = input()
strr = strr.split(',')
count = 0
for i in strr:
    if (i.isnumeric()):
        count+=1


print(count)