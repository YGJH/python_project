import hw_decorator
import itertools 
# 撰寫修飾子
def pretty(o_func):
    def n_func(*a,**k):
        return '$'+o_func(*a,**k)+'$'
    return n_func


@pretty
def f1(*args , **kwargs):
  return 'f1'

print(f1('aa'))

hw_decorator.checker(pretty)