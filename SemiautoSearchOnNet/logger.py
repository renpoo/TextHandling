# logger.py
import functools
import sys

def log_to_file(log_file):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            original_stdout = sys.stdout
            sys.stdout = open(log_file, 'a')
            try:
                result = func(*args, **kwargs)
            finally:
                sys.stdout.close()
                sys.stdout = original_stdout
            return result
        return wrapper
    return decorator
