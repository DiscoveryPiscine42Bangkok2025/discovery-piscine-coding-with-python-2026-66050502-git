a = input()
b = ""
for i in range(len(a)):
    if a[i] == a[i].upper():
        b+=a[i].lower()
    else:
        b+=a[i].upper()

print(b)
# Hello World
# hELLO wORLD
# ?>
# ?> ./up_low.py
# aaaaAAAA
# AAAAaaaa
# ?>
# ?> ./up_low.py
# hello 42
# HELLO 42