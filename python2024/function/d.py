import hw_hanoi

#define the generator hanoi
def hanoi(n,a,b,c):
    if(n == 1):
        yield a , c
    hanoi(n-1 , a , c , b)
    hanoi(1 , a , b , c)
    hanoi(n-1 , b , a , c)



print(hanoi(3 , 'a' , 'b' , 'c'))
hw_hanoi.checker(hanoi)