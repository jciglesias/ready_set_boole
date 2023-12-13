def adder(a, b):
    if isinstance(a, int) and isinstance(b, int):
        while a:
            c = a & b
            b = b ^ a
            a = c << 1
        return b
    return