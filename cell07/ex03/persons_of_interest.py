#!/usr/bin/env python


def famous_births(dict):
    def get_date_of_birth(x):
        return x["date_of_birth"]

    sorted_items = sorted(dict.values(), key=get_date_of_birth)
    for person in sorted_items:
        print(
            f"{person['name']} is a great scientist born in {person['date_of_birth']}."
        )


women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecilia": {"name": "Cecila Payne", "date_of_birth": "1900"},
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906"},
}
famous_births(women_scientists)
