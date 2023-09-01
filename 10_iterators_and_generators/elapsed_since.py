from time import perf_counter

def iter_time_elapsed(iterable):
    """
    A generator function that loops through an iterable and yields the time
    elapsed during each iteration.
    """
    
    for element in iterable:
        t_start = perf_counter()
        t_stop = perf_counter()
        t_elapsed = t_stop - t_start
        
        yield (t_elapsed, element)

for a_letter in iter_time_elapsed('to be or not to be'):
    print(a_letter)
    