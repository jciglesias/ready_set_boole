from string import ascii_uppercase

n_dir = {
    "&": lambda a, b: f"{a}{b}!|",
    "|": lambda a, b: f"{a}{b}!&",
    "=": lambda a, b: f"{a}{b}&{a}!{b}!&|",
    "^": lambda a, b: f"{a}{b}^",
    ">": lambda a, b: f"{a}{b}|",
}

eval_dir = {
    "&": lambda a, b: f"{a}{b}&",
    "|": lambda a, b: f"{a}{b}|",
    "=": lambda a, b: f"{a}{b}{a}!{b}!&&|",
    "^": lambda a, b: f"{a}{b}^",
    ">": lambda a, b: f"{a}!{b}|",
}

def conjunctive_normal_form(formula: str) -> str:
    if isinstance(formula, str) and len(formula) > 2:
        stack = []
        for elem in formula:
            if elem in ascii_uppercase:
                stack.append(elem)
            elif elem in "&|^>=":
                right = stack.pop()
                left = stack.pop()
                if left[-1] != elem:
                    stack.append(eval_dir[elem](left, right))
                else:
                    i = 1
                    while left[-i] == elem: i += 1
                    stack.append(eval_dir[elem](left[:1-i], right) + left[1-i:])
            elif elem == "!":
                stack.append(negative_form(stack.pop(), 1))
            else:
                print("bad character in formula: ", elem)
                return
        return stack.pop()
    return formula

def negative_form(formula: str, negate: bool) -> str:
    if isinstance(formula, str) and len(formula) > 2:
        stack = []
        for elem in formula:
            if elem in ascii_uppercase:
                stack.append(elem)
            elif elem in "&|^>=":
                right = stack.pop()
                left = stack.pop()
                if (negate):
                    stack.append(n_dir[elem](negative_form(left, 0), right))
                else:
                    stack.append(left + "!" + right + "!" + elem)
        return stack.pop()
    return formula + "!"