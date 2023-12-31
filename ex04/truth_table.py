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
    if isinstance(formula, str):
        stack = []
        for elem in formula:
            if elem in "01":
                stack.append(bool(int(elem)))
            elif elem in "&|^>=":
                try:
                    right = stack.pop()
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

def parsing(variables: list):
    for v in variables:
        if v not in list(string.ascii_uppercase):
            exit(f"Bad character in formula: {v}")
    variables.sort()
    return variables

def print_truth_table(formula: str):
    variables = parsing(list("".join(set(formula)).replace("&", "").replace("|", "").replace("^", "").replace(">", "").replace("=", "").replace("!", "")))
    dir = {elem: 0 for elem in variables}
    for v in dir:
        print("|",v, end=" ")
    print("| = |")
    for _ in dir:
        print("|---", end="")
    print("|---|")
    print_truth_line(dir, evaluate(dir, formula))
    recursiv(dir, len(variables), variables, formula)


def recursiv(dir, i, variables: str, formula):
    if (i):
        tmp = copy(dir)
        for a in [0, 1]:
            tmp[variables[i-1]] = a
            if (tmp != dir):
                print_truth_line(tmp, evaluate(tmp, formula))
            recursiv(tmp, i - 1, variables, formula)
    return

def evaluate(dir, formula: str):
    tmp = copy(formula)
    for a in dir:
        tmp = tmp.replace(a, str(dir[a]))
    return int(eval_formula(tmp))

def print_truth_line(dir, truth):
    for i in dir:
        print("|", dir[i], end=" ")
    print("|", truth,"|")
