class Error:
    def __init__(self, description, path, lineNum, pos, line):
        self.description = description
        self.path = path
        self.lineNum = lineNum
        self.pos = pos
        self.line = line
    
    def fire(self):
        print(f"Error decoding {self.path} line {self.lineNum}: {self.description}, but whatever, let's just ignore it for now!")
        print("-----Your fking code-----")
        print(self.line)
        print(" " * self.pos + "^")
        print("------------------------")