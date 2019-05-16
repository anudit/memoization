import time
from functools import lru_cache

def timeit(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    print(f'Duration: {time.time() - start}s')
    return result

def fib(number: int) -> int:
    if number == 0: return 0
    if number == 1: return 1
    return fib(number-1) + fib(number-2)

@lru_cache(maxsize=512)
def fibm(number: int) -> int:
    if number == 0: return 0
    if number == 1: return 1
    return fibm(number-1) + fibm(number-2)

print(timeit(fib, 30))
print(timeit(fibm, 30))
print(fibm.cache_info())
