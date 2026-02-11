#!/usr/bin/env python

numbers1 = [1, 2, 3, 4, 5]
numbers2 = []

for i in range(len(numbers1)):
    numbers2.append(numbers1[i] + 2)

print(f"Original array: {numbers1}")
print(f"New array: {numbers2}")
