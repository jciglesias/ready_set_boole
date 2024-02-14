from string import ascii_uppercase
from binarydoublechainedtree import BinaryDoubleChainedTree as bt
from binarydoublechainedtree import print_tree, create_node, negative_node,create_tree

n_dir = {
    # Disjunction (and) ¬(A ∧ B) ↔ (¬A ∨ ¬B)
    "&": lambda a,b: create_node(negative_node(a), "|", negative_node(b)),
    # Conjunction (or) ¬(A ∨ B) ↔ (¬A ∧ ¬B)
    "|": lambda a,b: create_node(negative_node(a), "&", negative_node(b)),
    # Exclusive disjunction (xor) ¬(A ⊻ B) ↔ ((A ∧ B) ∨ (¬A ∧ ¬B))
    "^": lambda a,b: create_node(create_node(a,"&",b),"|",create_node(negative_node(a),"&",negative_node(b))),
    # Material condition ¬(A ⇒ B) ⇔ (A ∧ ¬B)
    ">": lambda a,b: create_node(a, "&", negative_node(b)),
    # Logical equivalence ¬(A ⇔ B) ⇔ ((¬A ∨ ¬B) ∧ (A ∨ B))
    "=": lambda a, b: create_node(create_node(negative_node(a),"|",negative_node(b)),"&",create_node(a,"|",b)),
}

eval_dir = {
    # Disjunction (and) A ∧ B
    "&": lambda a,b: create_node(a, "&", b),
    # Conjunction (or) A ∨ B
    "|": lambda a,b: create_node(a, "|", b),
    # Exclusive disjunction (xor) A ⊻ B ↔ ((¬A ∨ ¬B) ∧ (A ∨ B))
    "^": lambda a,b: create_node(create_node(negative_node(a),"|",negative_node(b)),"&",create_node(a,"|",b)),
    # Material condition (A ⇒ B) ⇔ (¬A ∨ B)
    ">": lambda a,b: create_node(negative_node(a), "|", b),
    # Logical equivalence (A ⇔ B) ⇔ ((A ∧ B) ∨ (¬A ∧ ¬B))
    "=": lambda a, b: create_node(create_node(a,"&",b),"|",create_node(negative_node(a),"&",negative_node(b))),
}

truth = {
    "&": lambda a, b: a & b,
    "|": lambda a, b: a | b,
    "l": {
        "&": lambda a, b: b - a,
        "|":lambda a, b: b,
    },
    "r": {
        "&": lambda a, b: a - b,
        "|": lambda a, b: a,
    },
    "b": {
        "&": lambda a, b: set({}),
        "|": lambda a, b: (a | b) - (a & b),
    },
}

def eval_set(formula: str, sets: list) -> list:
    variables = parsing(list("".join(set(formula)).replace("&", "").replace("|", "").replace("^", "").replace(">", "").replace("=", "").replace("!", "")))
    var = {variables[i]: sets[i] for i in range(len(variables))}
    root = nnf_tree(create_tree(formula))
    tree_replace(root, var)
    tree_eval(root)
    return root.value if len(root.value) else {}

def tree_eval(root: bt):
    if root:
        tree_eval(root.left)
        tree_eval(root.right)
        if isinstance(root.value, str) and root.value in "&|":
            root.value = conjunction_eval(root.left, root.value, root.right)
        if root.value == "!" and not root.up:
            root.value = {}

def conjunction_eval(left: bt, conj: str, right: bt):
    if left.value != "!" and right.value != "!":
        return truth[conj](left.value, right.value)
    elif left.value == "!" and right.value != "!":
        return truth["l"][conj](left.left.value, right.value)
    elif left.value != "!" and right.value == "!":
        return truth["r"][conj](left.value, right.left.value)
    elif left.value == "!" and right.value == "!":
        return truth["b"][conj](left.left.value, right.left.value)

def tree_replace(root: bt, var: dict):
    if root:
        tree_replace(root.left, var)
        tree_replace(root.right, var)
        if isinstance(root.value, str) and root.value in ascii_uppercase:
            root.value = set(var[root.value])


def nnf_tree(root: bt) -> bt:
    current = root
 
    while current:
        if current.value in "|&>^=":
            tmp = eval_dir[current.value](current.left, current.right)
            current.value = tmp.value
            current.left = tmp.left
            current.right = tmp.right
        elif current.value == "!":
            tmp = negative_eval(current.left)
            current.value = tmp.value
            current.left = tmp.left
            current.right = tmp.right
        if current.right != None:
            current.right = nnf_tree(current.right)
            current.right.up = current
        current = current.left
    return root

def negative_eval(root: bt):
    if root.value in ascii_uppercase:
        return negative_node(root)
    elif root.value == "!":
        return root.left
    else:
        return n_dir[root.value](root.left, root.right)


def parsing(variables: list):
    for v in variables:
        if v not in ascii_uppercase:
            exit("Not valid formula")
    variables.sort()
    return variables
