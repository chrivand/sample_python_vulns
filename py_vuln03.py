# -*- coding: utf-8 -*-
# set variable to assert
var_to_assert = "hello"

# if condition returns True, then nothing happens:
assert var_to_assert == "hello"

# if condition returns False, AssertionError is raised (comment out to test the next one):
assert var_to_assert == "goodbye"

# if condition returns False, custom AssertionError is raised: 
assert var_to_assert == "goodbye", f"var_to_assert should be '{var_to_assert}'"

# run like this to disable assert statements: python3 -O py_vuln03.py
print("When you run code with -O, assert statements are skipped...")