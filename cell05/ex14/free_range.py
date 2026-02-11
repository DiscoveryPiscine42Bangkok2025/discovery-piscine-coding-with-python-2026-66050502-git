#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print("none")
else:
    a= []
    for i in range(int(sys.argv[1]), int(sys.argv[2])+1):
        a.append(i)
    print(a)


        # ?> ./free_range.py | cat -e
# none$
# ?> ./free_range.py 10 14 | cat -e
# [10, 11, 12, 13, 14]$
# ?>
