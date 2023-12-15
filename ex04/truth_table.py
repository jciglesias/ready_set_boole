from copy import copy

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

def print_truth_table(formula: str):
    variables = list("".join(set(formula)).replace("&", "").replace("|", "").replace("^", "").replace(">", "").replace("=", "").replace("!", ""))
    variables.sort()
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
