# -*- coding: utf-8 -*-
import os

# /Users/christophervandermade/Documents/GitHub/sample_python_vulns/foo/bar.txt
# foo/bar.txt
# /Users/christophervandermade/../../../etc/area51.txt [will not work but could be something malicious]

file_location = input('\nType location: ') # /Users/christophervandermade/../../../../etc/area51.txt

# open and read file
file = open(file_location, "r")
print(f"File content:\n{file.read()}")