from string import ascii_uppercase
from copy import deepcopy
from binarydoublechainedtree import BinaryDoubleChainedTree as bt

n_dir = {
    # Disjunction (and) ¬(A ∧ B) ↔ (¬A ∨ ¬B)
    "&": lambda a,b: create_node(negative_node(a), "|", negative_node(b)),
    # Conjunction (or) ¬(A ∨ B) ↔ (¬A ∧ ¬B)
    "|": lambda a,b: create_node(negative_node(a), "&", negative_node(b)),
    # Exclusive disjunction (xor) ¬(A ⊻ B) ↔ ((A ∧ B) ∨ (¬A ∧ ¬B))
    "^": lambda a,b: create_node(create_node(a,"&",b),"|",create_node(negative_node(a),"&",negative_node(b))),
    # Material condition ¬(A ⇒ B) ⇔ (A ∧ ¬B)
    ">": lambda a,b: create_node(negative_node(a), "|", b),
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

def negation_normal_form(f: str) -> str:
    root = create_tree(f)
    r = tree_eval(root)
    line = []
    print_tree(r, line)
    return(''.join(line))

def tree_eval(root: bt) -> bt:
    current = root
 
    while current:
        if current.value in "|&>^=":
            if current.up == None:
                tmp = eval_dir[current.value](current.left, current.right)
                current.value = tmp.value
                current.left = tmp.left
                current.right = tmp.right
            else:
                tmp = eval_dir[current.value](current.left, current.right)
                tmp.up = current.up
                if current.up.left == current:
                    current.up.left = tmp
                else:
                    current.up.right = tmp
                current = tmp
            if current.right != None:
                current.right = tree_eval(current.right)
                current.right.up = current
        elif current.value == "!":
            tmp = negative_eval(current.left)
            current.value = tmp.value
            current.left = tmp.left
            current.right = tmp.right
        current = current.left
    return root

def negative_eval(root: bt):
    if root.value in ascii_uppercase:
        return negative_node(root)
    elif root.value == "!":
        return root.left
    else:
        return n_dir[root.value](root.left, root.right)

def create_node(left: bt, value, right: bt):
    new_node = bt(value)
    left.up = new_node
    new_node.left = left
    right.up = new_node
    new_node.right = right
    return new_node

def negative_node(left: bt):
    new_node = bt("!")
    left.up = new_node
    new_node.left = left
    return new_node

def print_tree(root: bt, line: list = []):
    if root:
        print_tree(root.left, line)
        if root.value in ascii_uppercase or root.value == "!":
            line.append(root.value)
        elif root.value in "&^|=>":
            print_tree(root.right, line)
            line.append(root.value)
    # return line

def create_tree(formula: str):
    if isinstance(formula, str):
        stack = []
        for elem in formula:
            node = bt(elem)
            if elem in "&|^>=":
                try:
                    right = stack.pop()
                    left = stack.pop()
                except:
                    exit("Bad formula")
                left.up = node
                right.up = node
                node.left = left
                node.right = right
            elif elem == "!":
                node.left = stack.pop()
                node.left.up = node
            elif elem not in ascii_uppercase:
                exit(f"bad character in formula: {elem}")
            stack.append(node)
        return stack.pop()
    return
