print("The name of his module is {}".format(__name__)) #tells you the name of what python think this module is

import second_program


# The code you want to run, always put into the following block
# always put into an if__name __ == "__main__": block




# Tip 1: Can import file as an alias
# Example

import calculator as calc # calc acts as an alias
#Still need to specify it is from calc module
HDL_driver()
print("oopsie")


# Tip 2: Don't have to import whole file
from calculator import HDL_driver #don't specify parenthesis when importing # importing just the HDL_driver

# Don't even need to specify what module it is from now.
HDL_driver()
