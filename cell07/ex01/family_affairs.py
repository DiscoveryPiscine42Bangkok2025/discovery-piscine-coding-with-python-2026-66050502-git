#!/usr/bin/env python3

def find_the_redheads(d):
    return filter(d)
def filter(d):
    a = []
    for k, v in d.items():
        if v == "red":
            a.append(k)
    return a
dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))