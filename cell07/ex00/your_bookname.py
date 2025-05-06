#!/usr/bin/python3 

def array_of_names(name) :
    newName = [f"{k.title()} {v.title()}" for k, v in name.items()]
    return newName

person = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(person))