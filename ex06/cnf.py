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

def conjunctive_normal_form(f: str) -> str:
    root = create_tree(f)
    tree_eval(root)
    cnf_tree(root)
    line = []
    print_tree(root, line)
    return("".join(line))

def tree_eval(root: bt) -> bt:
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
            current.right = tree_eval(current.right)
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
    
def cnf_tree(root: bt):
    if root:
        cnf_tree(root.left)
        cnf_tree(root.right)
        if root.value in "&|" and root.up and root.up.value in "&|":
            cnf_rearrange(root.up)

def cnf_rearrange(root: bt):
    if root.value == "|" and ((root.left and root.left.value == "&") or (root.right and root.right.value == "&")):
        if root.left and root.left.value == "&":
            pass # A | (B & C) = (A | B) & (A | C)
        if root.right and root.right.value == "&":
            pass # A | (B & C) = (A | B) & (A | C)
    elif root.value == "&" and ((root.left and root.left.value == "|") or (root.right and root.right.value == "|")):
        if root.left and root.left.value == "|":
            pass # A & (B | C) = (A & B) | (A & C)
        if root.right and root.right.value == "|":
            pass