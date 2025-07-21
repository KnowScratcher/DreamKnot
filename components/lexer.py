"""
lexer
"""

from components import asn
from components.asn import *
from components.error import Error
import re

var = {
    "out": asn.Print
}

class Lexer:
    def __init__(self) -> None:
        self.text: str | None = None
        self.path: str = "unknown"
        self.head: Node = Node()
        self.curr: Node | None = self.head


    def getLines(self, string: str):
        return string.split("\n")
    
    def checkClosure(self, string: str):
        bal = 0
        strLock = False
        for i in range(len(string)):
            if (string[i] == "\"" or string[i] == "\'") and (i > 0 and string[i - 1] != "\\"):
                strLock = not strLock
            elif string[i] == "(" and not strLock:
                bal += 1
            elif string[i] == ")" and not strLock:
                bal -= 1
            if bal < 0:
                return False
        return bal == 0

    def decodeLine(self, line: str, lineNum: int) -> None:
        if re.search(r".*\(.*\).*", line): # if the line has ()
            if self.checkClosure(line):
                split:list[str] = re.split(r"([^(]*)\((.*)\)", line)[1:-1]
                if split[0] in var:
                    if var[split[0]] is Print:
                        split[1] = re.sub(r"\\\'", "\'", split[1])
                        split[1] = re.sub(r"\\\"", "\"", split[1])
                        if len(split[1]) > 1 and ((split[1].startswith("\"") and split[1].endswith("\"")) or (split[1].startswith("\'") and split[1].endswith("\'"))):
                            split[1] = split[1][1:-1]
                        self.curr.child = Print(str(split[1])) # type: ignore
                        self.curr = self.curr.child # type: ignore
            else:
                Error("Unclosed parenthesis", self.path, lineNum, len(line), line).fire()
        else:
            Error("WTF is this", self.path, lineNum, 0, line).fire()

    def decode(self, string: str, path:str) -> Node:
        self.path = path
        lines = self.getLines(string)
        for index, line in enumerate(lines):
            self.decodeLine(line, index + 1)
        return self.head