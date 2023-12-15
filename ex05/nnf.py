from string import ascii_uppercase

eval_dir = {
    "&": lambda a, b: f"{a}{b}|",
    "|": lambda a, b: f"{a}{b}&",
    "=": lambda a, b: f"{a}{b}&{a}!{b}!&|",
    "^": lambda a, b: f"{a}{b}^",
    ">": lambda a, b: f"{a}!{b}|",
    "!": lambda a: negation_form(a),
}

def negation_normal_form(formula: str) -> bool:
    if isinstance(formula, str) and len(formula) > 2:
        stack = []
        for elem in formula:
            if elem in ascii_uppercase:
                stack.append(elem)
            elif elem in "&|^>=":
                right = stack.pop()
                left = stack.pop()
                stack.append(eval_dir[elem](left, right))
            elif elem == "!":
                stack.append(eval_dir[elem](stack.pop()))
            else:
                print("bad character in formula: ", elem)
                return
        return stack.pop()
    print("Formula should be a string bigger than 2 char")

def negation_form(formula: str) -> str:
    ret = ""
    for a in formula:
        if a in ascii_uppercase:
            ret += a + "!"
        else:
            ret += a
    return ret