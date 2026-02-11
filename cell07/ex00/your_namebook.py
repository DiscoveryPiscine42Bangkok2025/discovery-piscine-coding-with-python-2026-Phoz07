#!/usr/bin/env python

def array_of_names(dict):
    names = []
    for key, value in dict.items():
        names.append(key.capitalize() + " " + value.capitalize())
    return names

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindaciers",
}

print(array_of_names(persons))
