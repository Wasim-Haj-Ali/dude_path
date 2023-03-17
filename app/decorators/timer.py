from time import perf_counter
from functools import wraps


def benchmark(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        start_time = perf_counter()
        func(*args, **kwargs)
        end_time = perf_counter() - start_time
        print(f"{func.__name__} took {end_time} seconds.")
        
    return wrapper