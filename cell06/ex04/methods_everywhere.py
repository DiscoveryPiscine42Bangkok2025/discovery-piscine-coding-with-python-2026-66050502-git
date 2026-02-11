#!/usr/bin/env python3

# /methods_everywhere.py | cat -e
# none$
# ?> ./methods_everywhere.py 'lol' 'physically' 'backpack' | cat -e
# lolZZZZZ$
# physical$
# backpack$
import sys
def shrink(s):
    print(s[:8])
def enlarge(s):
    while len(s) < 8:
        s+="Z"
    print(s)

if len(sys.argv) == 1:
    print("none")
else:
    for i in range(1, len(sys.argv) ):
        if len(sys.argv[i]) > 8:
            shrink(sys.argv[i])
        else:
            enlarge(sys.argv[i])

