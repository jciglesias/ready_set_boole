eval_dir = {
    "&": lambda a, b: a & b,
    "|": lambda a, b: a | b,
    "=": lambda a, b: a == b,
    "^": lambda a, b: a ^ b,
    ">": lambda a, b: a != True or b == True,
    "!": lambda a: not a,
}

def eval_formula(formula: str) -> bool:
    if isinstance(formula, str) and len(formula) > 2:
        stack = []
        for elem in formula:
            if elem in "01":
                stack.append(bool(int(elem)))
            elif elem in "&|^>=":
                right = stack.pop()
                left = stack.pop()
                stack.append(eval_dir[elem](right, left))
            elif elem == "!":
                stack.append(eval_dir[elem](stack.pop()))
            else:
                print("bad character in formula: ", elem)
                return
        return stack.pop()
    print("Formula should be a string bigger than 2 char")