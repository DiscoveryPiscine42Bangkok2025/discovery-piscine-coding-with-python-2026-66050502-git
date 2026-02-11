#!/usr/bin/env python3
import sys
def downcase_it(s):
    return s.lower()

if len(sys.argv) == 1:
    print('none')
else:
    for i in range(1, len(sys.argv)):
        print(downcase_it(sys.argv[i]))

#  ./downcase_all.py
# none
# ?> ./downcase_all.py "HELLO WORLD" "I understood Arrays well!"
# hello world
# i understood arrays well!