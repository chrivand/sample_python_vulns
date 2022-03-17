import os

file_location = input('\nType location: ') # /Users/christophervandermade/../secrets.txt
print(file_location)
real_path = os.path.realpath(file_location)
print(real_path)
os.path.split(real_path) == True