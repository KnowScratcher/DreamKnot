import argparse
from components import ast, lexer
import os

parser = argparse.ArgumentParser(description="A script that says hello.")
parser.add_argument("file", type=str, help="run code in file.", nargs="?")
# parser.add_argument("-c", "--cmd", type=str, help="run code on command line.")
# parser.add_argument("-f", "--file", type=str, help="run code in file.")
args = parser.parse_args()

if args.file is None:
    print("No file selected, exiting")
    exit()
if not os.path.exists(args.file):
    print(f"File {args.file} does not exist, exiting")
    exit()

astParser = ast.AstParser(lexer.Lexer())
astParser.parseFromFile(args.file)
astParser.execute()