x = "hello"

# if condition returns True, then nothing happens:
assert x == "hello"

# if condition returns False, AssertionError is raised:
assert x == "goodbye"

# if condition returns False, custom AssertionError is raised: 
assert x == "goodbye", "x should be 'hello'"

# run like this to disable asserts: python -O py_vuln03.py
