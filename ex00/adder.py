from copy import copy

def adder(x, y):
    if isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0:
        a, b = copy(x), copy(y)
        while a:
            c = a & b
            b = b ^ a
            a = c << 1
        return b
    return