#!/usr/bin/env python3

# Create a program called scope_that.py that does not take any parameters.
# • This program must be executable.
# • Inside the program, create a method called add_one that takes a parameter and
# adds 1 to the parameter passed to the method.
# • Initialize a variable in the body of the program, display it, and then call the method
# that adds 1.
# • Display your variable again in the body of the program.
# • What do you observe?

def add_one(a):
    a += 1

eight = 8
print(eight)
add_one(eight)
print(eight)

# observe nothing