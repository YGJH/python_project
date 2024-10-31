import functools
import time


@functools.cache
def comb(m , n):
    if n == 1:
        return m
    elif n == m:
        return 1
    else:
        return comb(m-1 , n) + comb(m-1 , n-1)

@functools.lru_cache(maxsize=2) # only keep 2 most recent calls
def comb_lru_cache(m , n):
    if n == 1:
        return m
    elif n == m:
        return 1
    else:
        return comb_lru_cache(m-1 , n) + comb_lru_cache(m-1 , n-1)

def comb_without_cache(m , n):
    if n == 1:
        return m
    elif n == m:
        return 1
    else:
        return comb_without_cache(m-1 , n) + comb_without_cache(m-1 , n-1)

for f in [comb , comb_lru_cache , comb_without_cache]:
    if hasattr(f , 'cache_clear'):
        print('clear cache')
        f.cache_clear()
    m , n = 30 , 15

    t0 = time.time()
    x = f(m , n)
    print(f'answer {x} computin time for the 1st call to {f.__name__}({m},{n}):{time.time()-t0} second')
    
    t0 = time.time()
    x = f(m , n)
    print(f'answer {x} computin time for the 1st call to {f.__name__}({m},{n}):{time.time()-t0} second')

print(comb.cache_info())
print(comb_lru_cache.cache_info())
