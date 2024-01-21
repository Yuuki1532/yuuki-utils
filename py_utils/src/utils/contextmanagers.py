import time
from contextlib import contextmanager

@contextmanager
def print_timeit():
    """
    Times and prints the time interval within the context manager block
    """
    t1 = time.perf_counter()
    yield
    print(f'time elapsed: {time.perf_counter() - t1} s')
