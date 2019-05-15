from time import clock
def simpleRec(n):
    if n == 1:
        return n
    else:
        return n*simpleRec(n-1)

def timeit(func, *args, **kwargs):
    starting_time = clock()
    result = func(*args, **kwargs)
    ending_time = clock()
    print('Duration: {}'.format(ending_time - starting_time))
    return result

simpleRec(5)
timeit(simpleRec, 5)
