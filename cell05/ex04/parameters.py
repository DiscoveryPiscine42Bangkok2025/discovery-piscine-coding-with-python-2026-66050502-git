#!/usr/bin/env python3



import sys
print(f"Number of parameters: {len(sys.argv) - 1}.")


# Number of parameters: 0.
# ?> ./parameters.py "initiation"
# Number of parameters: 1.
# ?> ./parameters.py "this" "is" "crazy" "there's" "everywhere!"
# Number of parameters: 5.