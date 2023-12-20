eval_dir = {
    "&": lambda a, b: a & b,
    "|": lambda a, b: a | b,
    "=": lambda a, b: a == b,
    "^": lambda a, b: a ^ b,
    ">": lambda a, b: a != True or b == True,
    "!": lambda a: not a,
}

def eval_formula(formula: str) -> bool:
    if isinstance(formula, str):
        stack = []
        for elem in formula:
            if elem in "01":
                stack.append(bool(int(elem)))
            elif elem in "&|^>=":
                right = stack.pop()
                try:
                    left = stack.pop()
                except:
                    exit("Bad formula")
                stack.append(eval_dir[elem](left, right))
            elif elem == "!":
                stack.append(eval_dir[elem](stack.pop()))
            else:
                exit(f"Bad character in formula: {elem}")
        return stack.pop()
    return