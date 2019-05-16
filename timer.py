import time

def timeit(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    print(f'Duration: {time.time() - start}s')
    return result
