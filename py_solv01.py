# -*- coding: utf-8 -*-
import os

# set safe directory
safe_dir = "/Users/christophervandermade/Documents/GitHub/sample_python_vulns/"

# /Users/christophervandermade/Documents/GitHub/sample_python_vulns/foo/bar.txt
# /Users/christophervandermade/../../../etc/area51.txt

# ask for user input
requested_path = input('\nType location: ') 
print(f"Inputted file path: {requested_path}\n")

# clean input
requested_real_path = os.path.realpath(requested_path)
print(f"Real file path: {requested_real_path}\n")

# print longest common prefix
prefix = os.path.commonprefix((requested_real_path,safe_dir))
print(f"Longest common path prefix: {prefix}\n")

# check if prefix is same as safe_dir
if prefix != safe_dir: 
    # malicious user!
    raise Exception("Requested directory not same as safe_dir!")
else:
    # safe user
    print("Requested directory same as safe_dir!\n")
    # open and read file
    file = open(requested_real_path, "r")
    print(f"File content:\n{file.read()}")