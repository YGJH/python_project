import ast
import sys
import math


def cos(x):
    return math.cos(x * math.pi/180)

def sin(x):
    return math.sin(x*math.pi/180)

def bye():
    exit()

def str2obj(s , local_dict):
    exec('__ps='+s , globals(), local_dict)
    a = local_dict['__ps']
    return a
local_dic = dict()

while 1:
    _s = input()
    if _s.find('<-') != -1:
        _ss = _s.split('<-')
        local_dic[_ss[0]] = str2obj(_ss[1],local_dic)
    else:
        exec(_s , globals() ,local_dic) 

