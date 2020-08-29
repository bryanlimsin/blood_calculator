print("The name of this module is {}".format(__name__)) # tells you the name of what python think this module is

import second_program # To run this successfully from Spyder, I need to set the path to where what I want to import is
# It is easy at the command line if the 2 files are in the same location


# The code you want to run, always pu1t into the following block
# always put into an if__name __ == "__main__": block






# Tip 1: Can import file as an alias
# Example

import calculator as calc # calc acts as an alias
# Still need to specify it is from calc module
calc.HDL_driver()
print("oopsie")


# Tip 2: Don't have to import whole file
#from calculator import HDL_driver # don't specify parenthesis when importing # importing just the HDL_driver

# Don't even need to specify what module it is from now.
HDL_driver() # Only if had a from statement initially


