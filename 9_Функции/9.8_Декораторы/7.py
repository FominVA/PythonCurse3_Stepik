import functools

def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(start, end+1):
                result = str(func(*args, **kwargs)).replace(str(func(*args, **kwargs))[i], char, 1)
            return result
        return wrapper
    return decorator

@strip_range(3, 5)
def beegeek():
    return 'beegeek'
    
print(beegeek())