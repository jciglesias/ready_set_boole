from typing import Optional
import binarytree
from binarytree import Node, NodeValue
from string import ascii_uppercase

class BinaryDoubleChainedTree(binarytree.Node):
    up: binarytree.Node

    def __init__(self, value: NodeValue, left: Node | None = None, right: Node | None = None, up: Node | None = None) -> None:
        super().__init__(value, left, right)
        self.up = up

def create_tree(formula: str):
    if isinstance(formula, str):
        stack = []
        for elem in formula:
            node = BinaryDoubleChainedTree(elem)
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

def print_tree(root: Node, line: list):
    if root:
        print_tree(root.left, line)
        print_tree(root.right, line)
        if root.value in ascii_uppercase or root.value == "!":
            line.append(root.value)
        elif root.value in "&^|=>":
            line.append(root.value)

def create_node(left: BinaryDoubleChainedTree, value, right: BinaryDoubleChainedTree):
    new_node = BinaryDoubleChainedTree(value)
    left.up = new_node
    new_node.left = left
    right.up = new_node
    new_node.right = right
    return new_node

def negative_node(left: BinaryDoubleChainedTree):
    new_node = BinaryDoubleChainedTree("!")
    left.up = new_node
    new_node.left = left
    return new_node
