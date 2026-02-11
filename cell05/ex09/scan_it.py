#!/usr/bin/env python3


import sys

if len(sys.argv) == 2 or len(sys.argv) == 1:
    print('none')
else:
    print(sys.argv)
    c = 0
    for i in sys.argv[2].split(" "):
        if i == sys.argv[1]:
            c+=1
    print(c)


# ?> ./scan_it.py | cat -e
# none$
# ?> ./scan_it.py "the" | cat -e
# none$
# ?> ./scan_it.py "the" "the quick brown fox jumps over the lazy dog" | cat -e
# 2$
# ?>