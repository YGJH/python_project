import copy
import hw_mdl

#撰寫你的程式
def create_mdl(tp,default=None):
    if len(tp) == 0:
        return copy.copy(default)
    else:
        li = list()
        p = create_mdl(tp[1:] , default)
        for _ in range(tp[0]):
            li.append(copy.copy(p))
        return li

hw_mdl.checker(create_mdl)
print(1/0)
# p = create_mdl((3 , 4 ,5) , 0);
# print(id(p[0][0][0]))
# print(id(p[0][0][1]))