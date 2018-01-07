from lark import Lark

def ProgressionParser():
    with open('prog.g', 'r') as f:
        grammar = f.read()
    return Lark(grammar, start="progression")
