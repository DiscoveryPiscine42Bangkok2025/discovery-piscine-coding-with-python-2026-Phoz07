#!/usr/bin/env python

password = "Python is awesome"
password_input = input().strip()

if password_input == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
