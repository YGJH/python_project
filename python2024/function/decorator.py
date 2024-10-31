def logging(o_func):
    def pr(*args , **kwargs):
        print("{} this is function {} {}".format(o_func.__name__ , args , kwargs) )
        return o_func(*args , **kwargs)
    return pr


def mm(message1 , message2):
    print(message1 , message2)

mm = logging(mm)
mm('hello' , message2='h1')


# is equal to

@logging
def my_func(message1 , message2):
    print(message1 , message2)

my_func('11' , 'hello meow!')