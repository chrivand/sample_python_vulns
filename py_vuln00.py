# -*- coding: utf-8 -*-

# example code snippet py_vuln00: Arbitrary Code Execution:
compute_user_input = input('\nType something here to compute: ')
if not compute_user_input:
	print ("No input")
else:
	print ("Result: ", eval(compute_user_input))

# 2*2
# __import__("os").system("ls")
# __import__('os').system('rm –rf /') 
