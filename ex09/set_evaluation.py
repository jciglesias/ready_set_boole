from string import ascii_uppercase

truth = {
    "&": lambda a, b: a & b,
    "|": lambda a, b: a | b,
    "=": lambda a, b: a == b,
    "^": lambda a, b: a ^ b,
    ">": lambda a, b: set({}) | b,
    "!": lambda a: set({}) ,
}

def parsing(variables: list):
    for v in variables:
        if v not in ascii_uppercase:
            exit("Not valid formula")
    variables.sort()
    return variables

def eval_set(formula: str, sets: list) -> list:
    if isinstance(formula, str) and isinstance(sets, list):
        variables = parsing(list("".join(set(formula)).replace("&", "").replace("|", "").replace("^", "").replace(">", "").replace("=", "").replace("!", "")))
        var = {variables[i]: sets[i] for i in range(len(variables))}
        stack = []
        for elem in formula:
            if elem in ascii_uppercase:
                stack.append(set(var[elem]))
            elif elem in "&|>=^":
                try:
                    right = stack.pop()
                    left = stack.pop()
                except:
                    exit("Bad formula")
                stack.append(truth[elem](left, right))
            elif elem == "!":
                stack.append(truth[elem](stack.pop()))
            else:
                exit(f"Bad character in formula: {elem}")
        ret: set = stack.pop()
        return ret if len(ret) else {}
    exit("Formula must be a string and sets a list")