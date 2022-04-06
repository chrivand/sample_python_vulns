# -*- coding: utf-8 -*-
# example code snippet py_solv00: Arbitrary Code Execution
import ast
import astpretty

UNARY_OPS = (ast.UAdd, ast.USub)
BINARY_OPS = (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod)

def validate(user_input):
    """
    function that validates user input to be mathemetical expression
    """
    def _is_arithmetic(node):
        # print node for educational purposes
        print(f"Checking node: {node}")
        # check if node is a number
        if isinstance(node, ast.Num):
            return True
        # check if node is arithmetic symbol         
        elif isinstance(node, ast.Expression):
            return _is_arithmetic(node.body)
        # check if node is unary operation
        elif isinstance(node, ast.UnaryOp):
            valid_op = isinstance(node.op, UNARY_OPS)
            return valid_op and _is_arithmetic(node.operand)
        # check if node is binary operation
        elif isinstance(node, ast.BinOp):
            valid_op = isinstance(node.op, BINARY_OPS)
            return valid_op and _is_arithmetic(node.left) and _is_arithmetic(node.right)
        else:
            raise ValueError(f"Unsupported type {node}")
    
    try:
        # parse input to Abstract Syntax Tree
        ast_tree = ast.parse(user_input, mode='eval')
        
        # print AST (just for educational purposes)
        #astpretty.pprint(ast_tree)
        
        # run ast object through function to check nodes
        return _is_arithmetic(ast_tree)
    except (SyntaxError, ValueError):
        return False

# ask for input
compute_user_input = input('\nType something here to compute: ')
# input validation
if not compute_user_input:
	raise Exception("No input")
if validate(compute_user_input):
    print(f"Result: {eval(compute_user_input)}")
else:
	raise Exception(f"Error, not a mathemetical expression: {compute_user_input}")

# Possible inputs to test:
# 2*2
# __import__("os").system("ls")
# __import__('os').system('rm –rf /') [DANGEROUS, DO NOT RUN THIS!]