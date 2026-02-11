#!/usr/bin/env python3

def array_of_names(d):
    l = []
    for k, v in d.items():
        l.append(f"{k.capitalize()} {v.capitalize()}")
    return l
persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))


# ['Jean Valjean', 'Grace Hopper', 'Xavier Niel', 'Fifi Brindacier']