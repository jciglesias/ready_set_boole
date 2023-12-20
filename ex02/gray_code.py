def gray_code(n: int):
    if isinstance(n, int) and n >= 0:
        return n ^ (n >> 1)