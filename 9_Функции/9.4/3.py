def polynom(x):
    polynom.__dict__.setdefault('values', set())
    s = x**2+1
    polynom.values.add(s)
    return s