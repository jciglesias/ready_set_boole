from copy import copy
import string

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
                return 0
        return stack.pop()
    return 0

def parsing(variables: list):
    for v in variables:
        if v not in list(string.ascii_uppercase):
            exit()
    variables.sort()
    return variables

def sat(formula: str):
    variables = parsing(list("".join(set(formula)).replace("&", "").replace("|", "").replace("^", "").replace(">", "").replace("=", "").replace("!", "")))
    dir = {elem: 0 for elem in variables}
    if evaluate(dir, formula):
        return True
    lst = []
    recursiv(dir, len(variables), variables, formula, lst)
    for i in lst:
        if i:
            return True
    return False


def recursiv(dir, i, variables: str, formula, lst: list):
    if (i):
        tmp = copy(dir)
        for a in [0, 1]:
            tmp[variables[i-1]] = a
            if (tmp != dir):
                lst.append(evaluate(tmp, formula))
            recursiv(tmp, i - 1, variables, formula, lst)
    return

def evaluate(dir, formula: str):
    tmp = copy(formula)
    for a in dir:
        tmp = tmp.replace(a, str(dir[a]))
    return int(eval_formula(tmp))

