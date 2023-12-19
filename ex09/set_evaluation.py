from string import ascii_uppercase

truth = {
    "&": lambda a, b: a & b,
    "|": lambda a, b: a | b,
    "=": lambda a, b: a == b,
    "^": lambda a, b: a ^ b,
    ">": lambda a, b: a != True or b == True,
    "!": lambda a: {} ,
}

def parsing(variables: list):
    for v in variables:
        if v not in ascii_uppercase:
            print("Not valid formula")
            exit()
    variables.sort()
    return variables

def eval_set(formula: str, sets: list) -> list:
    if isinstance(formula, str) and isinstance(sets, list):
        variables = parsing(list("".join(set(formula)).replace("&", "").replace("|", "").replace("^", "").replace(">", "").replace("=", "").replace("!", "")))
        var = {variables[i]: sets[i] for i in range(len(variables))}
        stack = []
        for elem in formula:
            if elem in ascii_uppercase:
                stack.append(var[elem])
            elif elem in "&|>=":
                right = stack.pop()
                left = stack.pop()
                stack.append(truth[elem](left, right))
            elif elem == "!":
                stack.append(truth[elem](stack.pop()))
            else:
                print("Bad character in formula: ", elem)
                return
        return stack.pop()
    return