from copy import copy

def adder(x, y):
    a = copy(x)
    b = copy(y)
    if isinstance(a, int) and isinstance(b, int):
        while a:
            c = a & b
            b = b ^ a
            a = c << 1
        return b
    return

def multiplier(x, b):
    i, a = 0, 0
    while i < b:
        a = adder(a, x)
        i = adder(i, 1)
    return a