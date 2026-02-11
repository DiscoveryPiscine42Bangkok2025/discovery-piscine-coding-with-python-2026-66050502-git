#!/usr/bin/env python3

def famous_births(d):
    l = []
    for v in d.values():
        l.append(f"{v['name']} is a great scientist born in {v['date_of_birth']}.")
    for i in l:
        print(i)
women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)


    

# Ada Lovelace is a great scientist born in 1815.
# Lise Meitner is a great scientist born in 1878.
# Cecila Payne is a great scientist born in 1900.
# Grace Hopper is a great scientist born in 1906.