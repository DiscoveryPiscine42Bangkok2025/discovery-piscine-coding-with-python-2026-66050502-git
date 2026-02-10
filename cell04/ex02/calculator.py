# Give me the first number: 10
# Give me the second number: 2
# Thank you!
# 10 + 2 = 12
# 10 - 2 = 8
# 10 / 2 = 5
# 10 * 2 = 20

first = int(input("Give me the first number: "))
second = int(input("Give me the second number: "))
print("Thank you!")
print(f"{first} + {second} = {first + second}")
print(f"{first} - {second} = {first - second}")
print(f"{first} / {second} = {first // second}")
print(f"{first} * {second} = {first * second}")