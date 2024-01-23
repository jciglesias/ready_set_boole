from typing import Optional
import binarytree
from binarytree import Node, NodeValue

class BinaryDoubleChainedTree(binarytree.Node):
    up: binarytree.Node

    def __init__(self, value: NodeValue, left: Node | None = None, right: Node | None = None, up: Node | None = None) -> None:
        super().__init__(value, left, right)
        self.up = up
