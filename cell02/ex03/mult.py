first = int(input("Enter the first number:\n"))
second = int(input("Enter the second number:\n"))
res = first * second

print(f"{first} x {second} = {res}")

if res > 0:
    print("The result is positive.")
elif res < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")

# Enter the first number:
# 42
# Enter the second number:
# 42
# 42 x 42 = 1764
# The result is positive.
# $ ./mult.py
# Enter the first number:
# 78
# Enter the second number:
# -1
# 78 x -1 = -78
# The result is negative.
# $ ./mult.py
# Enter the first number:
# 72
# Enter the second number:
# 0
# 72 x 0 = 0
# The result is positive and negative.

