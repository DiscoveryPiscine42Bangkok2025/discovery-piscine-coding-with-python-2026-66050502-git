#!/usr/bin/env python3

# ?> ./string_are_arrays.py | cat -e
# none$
# ?> ./string_are_arrays.py "The character Z is not found in this string" | cat -e
# none$
# ?> ./string_are_arrays.py "The character z is found in this string" | cat -e
# z$
# ?> ./string_are_arrays.py "Zaz visits the zoo with Zazie" | cat -e
# zzz$
import sys

if len(sys.argv) == 1:
    print("none")
else:
    z = 0
    for i in sys.argv[1]:
        if "z" == i:
            z+=1
    if z == 0:
        print("none")
    else:
        print("z"*z)
    