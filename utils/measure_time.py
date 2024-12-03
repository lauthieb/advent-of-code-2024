import time
from functools import wraps


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"""Execution time {func.__name__}:
            {end_time - start_time:.6f} seconds"""
        )
        return result

    return wrapper
