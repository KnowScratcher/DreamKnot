"""
Abstract syntax tree parser.
"""

from components.lexer import Lexer
from components.asn import *

class AstParser:
    def __init__(self, lexer):
        self.lexer: Lexer = lexer
        self.linkedNodes: Node = Node()
        self.path: str = "unknown"
    
    def parseFromFile(self, path):
        self.path = path
        with open(path, "r", encoding="utf-8") as file:
            self.parse(file.read())

    def parse(self, string):
        self.linkedNodes = self.lexer.decode(string, self.path)

    def execute(self):
        curr = self.linkedNodes
        while curr:
            curr.execute()
            curr = curr.child