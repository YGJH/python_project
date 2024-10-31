import hw_lambda
import math
from functools import reduce
# 假設a為一個整數list
a = [1,2,-3,4,5,6,7,8,9]
def math(x):
    return math.exp(x)
# expr1寫出使用filter,選擇a裡正的且為3的倍數。[6,9]
# expr1='[b for b in a if b %3 ==0 and b > 0]' #將你的運算式填入字串'
expr1='filter(lambda x: x>0 and x % 3 == 0 , a if a else [])'
# print(expr1)
# expr2寫出使用map,將a裡的元素的對映至math.exp(-a)
expr2= 'map(lambda x :math.exp(-x) , a if a else [])' #將你的運算式填入字串
# print(expr2)
# expr3寫出使用reduce計算a裡的元素絕對值(abs(x))的和
expr3='reduce(lambda x, y: x+y , map(lambda x=0 : abs(x) , a if a else [0,0]))' #將你的運算式填入字串
# print(expr3)
hw_lambda.checker(expr1,expr2,expr3)