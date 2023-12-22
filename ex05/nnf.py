from string import ascii_uppercase
from copy import deepcopy
import binarytree as bt

n_dir = {
    "&": lambda a, b: f"{a}!{b}!|",
    "|": lambda a, b: f"{a}!{b}!&",
    "=": lambda a, b: f"{a}{b}&{a}!{b}!&|",
    "^": lambda a, b: f"{a}!{b}^",
    ">": lambda a, b: f"{a}!{b}|",
}

eval_dir = {
    "&": lambda a, b: f"{a}{b}&",
    "|": lambda a, b: f"{a}{b}|",
    "=": lambda a, b: f"{a}{b}&{a}!{b}!&|",
    "^": lambda a, b: f"{a}{b}^",
    ">": lambda a, b: f"{a}!{b}|",
}

def negation_normal_form(f: str) -> str:
    root = create_tree(f)
    r = tree_eval(root)
    print(r)
    print_tree(r)
    print()

def tree_eval(root: bt.Node) -> bt.Node:
    if root:
        root.left = tree_eval(root.left)
        root.right = tree_eval(root.right)
        if root.value in "&|^=>":
            if root.left.value in ascii_uppercase and root.right.value in ascii_uppercase:
                return create_tree(eval_dir[root.value](root.left.value, root.right.value))
        elif root.value == "!":
            return negation_eval(root)
    return root
    

def negation_eval(root: bt.Node) -> bt.Node:
    if root:
        root.left = negation_eval(root.left)
        root.right = negation_eval(root.right   )
        if root.value in "&|^=>":
            if root.left.value in ascii_uppercase and root.right.value in ascii_uppercase:
                return create_tree(n_dir[root.value](root.left.value, root.right.value))
        elif root.value == "!":
            return root
    return root

def print_tree(root: bt.Node):
    if root:
        print_tree(root.left)
        if root.value in ascii_uppercase or root.value == "!":
            print(root.value, end="")
        elif root.value in "&^|=>":
            print_tree(root.right)
            print(root.value, end="")
        # if root.left.value in ascii_uppercase and root.right.value in ascii_uppercase:
        #     print(root.left.value + root.right.value + root.value)
        # elif not root.right and root.left.value in ascii_uppercase:
        #     print(root.left.value + root.value)

def create_tree(formula: str):
    if isinstance(formula, str):
        stack = []
        for elem in formula:
            node = bt.Node(elem)
            if elem in "&|^>=":
                try:
                    right = stack.pop()
                    left = stack.pop()
                except:
                    exit("Bad formula")
                node.left = left
                node.right = right
            elif elem == "!":
                node.left = stack.pop()
            elif elem not in ascii_uppercase:
                exit(f"bad character in formula: {elem}")
            stack.append(node)
        return stack.pop()
    return

# def negation_normal_form(formula: str) -> bool:
#     if isinstance(formula, str):
#         stack = []
#         for elem in formula:
#             if elem in ascii_uppercase:
#                 stack.append(elem)
#             elif elem in "&|^>=":
#                 try:
#                     right = stack.pop()
#                     left = stack.pop()
#                 except:
#                     exit("Bad formula")
#                 stack.append(eval_dir[elem](negation_normal_form(left), right))
#             elif elem == "!":
#                 stack.append(negative_form(stack.pop(), 1))
#             else:
#                 exit(f"bad character in formula: {elem}")
#         return stack.pop()
#     return formula

# def negative_form(formula: str, negate: bool) -> str:
#     if isinstance(formula, str) and len(formula) > 2:
#         stack = []
#         for elem in formula:
#             if elem in ascii_uppercase:
#                 stack.append(elem)
#             elif elem in "&|^>=":
#                 right = stack.pop()
#                 left = stack.pop()
#                 if (negate):
#                     stack.append(n_dir[elem](negative_form(left, 0), right))
#                 else:
#                     stack.append(left + "!" + right + "!" + elem)
#         return stack.pop()
#     return formula + "!"