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

def multiplier(a, b):
    if isinstance(a, int) and isinstance(b, int) and a >= 0 and b >= 0:
        x,y = copy(a), copy(b)
        z = 0
        while y:
            if y & 1:
                z = adder(z, x)
            x <<= 1
            y >>= 1
        return z
    return