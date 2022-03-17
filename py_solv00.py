# example code snippet py_solv00: Arbitrary Code Execution
import ast

UNARY_OPS = (ast.UAdd, ast.USub)
BINARY_OPS = (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod)

def validate(user_input):
    """
    function that validates user input to be decimal and arithmetic symbol
    """
    def _is_arithmetic(node):
        if isinstance(node, ast.Num):
            return True
        elif isinstance(node, ast.Expression):
            return _is_arithmetic(node.body)
        elif isinstance(node, ast.UnaryOp):
            valid_op = isinstance(node.op, UNARY_OPS)
            return valid_op and _is_arithmetic(node.operand)
        elif isinstance(node, ast.BinOp):
            valid_op = isinstance(node.op, BINARY_OPS)
            return valid_op and _is_arithmetic(node.left) and _is_arithmetic(node.right)
        else:
            raise ValueError('Unsupported type {}'.format(node))

    try:
        return _is_arithmetic(ast.parse(user_input, mode='eval'))
    except (SyntaxError, ValueError):
        return False

# previous sample code
compute_user_input = input('\nType something here to compute: ')
if not compute_user_input:
	print("No input")
if validate(compute_user_input):
    print("Result: ", eval(compute_user_input))
else:
	print(f"Error, not a mathemetical expression: {compute_user_input}")

# __import__("os").system("ls")
# __import__(‘os’).system(‘rm –rf /’) 