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
    "=": lambda a, b: f"{a}{b}&{a}!{b}!&|",
    "^": lambda a, b: f"{a}{b}^",
    ">": lambda a, b: f"{a}!{b}|",
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
                stack.append(eval_dir[elem](negation_normal_form(left), right))
            elif elem == "!":
                stack.append(negative_form(stack.pop(), 1))
            else:
                print("bad character in formula: ", elem)
                return
            # print(stack)
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
            # print(stack)
        return stack.pop()
    return formula + "!"