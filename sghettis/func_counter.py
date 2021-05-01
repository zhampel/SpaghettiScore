from __future__ import print_function
import ast

# Adapted from
# stackoverflow.com/questions/37514636/good-way-to-count-number-of-functions-of-a-python-file-given-path

class FunctionCounter(ast.NodeVisitor):
    def __init__(self, filename):
        self.function_count = 0
        with open(filename) as f:
            module = ast.parse(f.read())
            self.visit(module)

    def visit_FunctionDef(self, node):
        print('function: {}'.format(node.name))
        self.function_count += 1

    ##Uncomment this to disable counting methods, properties within a class
    #def visit_ClassDef(self, node):
    #    pass
