import  sys
#This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter

locations = sys.path
#SYS path is a list of directories that Python interprets to search for when it starts up.
#The Pythonpath is a list of directories that the Python interpreter will search for when it tries to resolve a module name.
for i in locations:
    print(i)
