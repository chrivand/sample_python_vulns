# -*- coding: utf-8 -*-
import os

file_location = input('\nType location: ') # /Users/christophervandermade/../area51.txt
print(f"File path before: {file_location}\n")
real_path = os.path.realpath(file_location)
print(f"File path before: {real_path}")

# open and read file
#file = open(file_location, "r")
#print(file.read())