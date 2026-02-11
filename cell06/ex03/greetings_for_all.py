#!/usr/bin/env python3

# 
#  ?> cat greetings_for_all.py | cat -e
# # your method definition here
# greetings('Alexandra')
# greetings('Wil')
# greetings()
# greetings(42)
# will produce the following output:
# ?> ./greetings_for_all.py | cat -e
# Hello, Alexandra.$
# Hello, Wil.$
# Hello, noble stranger.$
# Error! It was not a name.$

def greetings(abc=''):
    if not isinstance(abc, str):
        print("Error! It was not a name.")
    elif abc:
        print(f"Hello, {abc}.")
    elif not abc:
        print("Hello, noble stranger.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)