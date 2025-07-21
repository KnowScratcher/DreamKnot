"""
Abstract syntax tree nodes control.
"""

from enum import Enum

class Type(Enum):
    ActionPrint = "print"

class Node:
    def __init__(self) -> None:
        self.child: Node | None = None

    def execute(self):
        pass


class Print(Node):
    def __init__(self, s: str) -> None:
        super().__init__()
        self.string = s
    
    def execute(self):
        print(self.string)