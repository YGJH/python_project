# import sys

# return_msg = []

# try:
#     r1 =Rectangle(10,10,100,100)
#     r2 =Rectangle(20,20,100,100)
#     r3 =Rectangle(5,5,1,1)

#     if r1.area != 10000:
#         raise Exception('Area error')
#     if (r1&r2).area != 8100 and (r1&r3).area != 0:
#         raise Exception('__and__ error')
#     if (r1|r3).area != 11025:
#         raise Exception('__or__ error')
    
# except Exception as e:
#     return_msg.append(f'[Tester]This program does not pass test case #0, code:180111[Tester]')
#     return_msg.append(f'[Tester]{e}[Tester]')
# else:
#     return_msg.append(f'[Tester]This program passes test case #0, code:980199[Tester]')

# try:
#     if str(r1)!='Rectangle:(10,10)-(110,110)':
#         raise Exception('__str__ error')
#     if r1 != eval(repr(r1)):
#         raise Exception('__repr__ or __eq__ error')
    
# except Exception as e:
#     return_msg.append(f'[Tester]This program does not pass test case #1, code:382111[Tester]')
#     return_msg.append(f'[Tester]{e}[Tester]')
# else:
#     return_msg.append(f'[Tester]This program passes test case #1, code:102199[Tester]')    

# for m in return_msg:
#     print('\n'+m,file=sys.stderr)    

print('g')