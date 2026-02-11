#!/usr/bin/env python3

# ?> ./append_it.py | cat -e
# none$
# ?> ./append_it.py "parallel" "egoism" "human" | cat -e
# parallelism$
# humanism$

import sys

if len(sys.argv) == 1:
    print("none")
else:
    for i in range(1, len(sys.argv)):
        if 'ism' not in sys.argv[i]:
            print(str(sys.argv[i])+'ism') # str -> if argv is number, bool, ...
        else:
            continue
        