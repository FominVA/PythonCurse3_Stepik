import functools

def add_attrs(**kwargs):
    def decorator(func):
        for attr_name, attr_value in kwargs.items():
            setattr(func, attr_name, attr_value)
        if not hasattr(func, 'name'):
             setattr(func, 'name', func.__name__)
        return func
    return decorator
             

@add_attrs(attr1='bee', attr2='geek')
def beegeek():
    return 'beegeek'
    
print(beegeek.attr1)
print(beegeek.attr2)