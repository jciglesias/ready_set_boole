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
        if root.value in "&|":
            cnf_rearrange(root)

def cnf_rearrange(root: bt):
    if root.value == "|":
        if root.left and root.left.value == "&" and (not root.right or root.right.value not in "|&"):
            # (B & C) | A = (A | B) & (A | C)
            node_swap(root, root.right, root.left.left, root.left.right, 0)
        elif root.left and root.left.value == "|":
            a = root.right
            c = root.left.right
            root.left = root.left.left
            root.right = create_node(c,"|", a)
            root.left.up = root
            root.right.up = root
        elif root.right and root.right.value == "&" and (not root.left or root.left.value not in "|&"):
            # A | (B & C) = (A | B) & (A | C)
            node_swap(root, root.left, root.right.left, root.right.right, 1)
    elif root.value == "&":
        if root.left and root.left.value == "|" and (not root.right or root.right.value not in "|&"):
            # A & (B | C) = (A & B) | (A & C)
            node_swap(root, root.right, root.left.left, root.left.right, 0)
        elif root.left and root.left.value == "&":
            a = root.right
            b:bt = root.left.left
            c = root.left.right
            root.left = b
            root.right = create_node(c,"&", a)
            root.left.up = root
            root.right.up = root
        elif root.right and root.right.value == "|" and (not root.left or root.left.value not in "|&"):
            # A & (B | C) = (A & B) | (A & C)
            node_swap(root, root.left, root.right.left, root.right.right, 0)

def node_swap(root: bt, a: bt, b: bt, c: bt, value):
    op = ["|", "&"]
    root.value = op[value]
    root.left = create_node(a, op[not value], b)
    root.right = create_node(a, op[not value], c)
    root.left.up = root
    root.right.up = root

