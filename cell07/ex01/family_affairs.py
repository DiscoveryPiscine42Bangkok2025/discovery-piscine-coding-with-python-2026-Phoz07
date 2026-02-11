#!/usr/bin/env python


def find_the_redheads(family):
    redheads = []
    for name, hair in family.items():
        if hair == "red":
            redheads.append(name)
    return redheads


dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red",
}
print(find_the_redheads(dupont_family))
