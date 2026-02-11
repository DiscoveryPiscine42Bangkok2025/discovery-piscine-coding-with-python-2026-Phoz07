#!/usr/bin/env python

numbers1 = [2, 8, 9, 48, 8, 22, -12, 2]
numbers2 = []

for i in range(len(numbers1)):
    if numbers1[i] > 5:
        numbers2.append(numbers1[i] + 2)

print(f"{numbers1}")
print(f"{numbers2}")
