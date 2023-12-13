def grey_code(n: int):
    if isinstance(n, int):
        return n ^ (n >> 1)