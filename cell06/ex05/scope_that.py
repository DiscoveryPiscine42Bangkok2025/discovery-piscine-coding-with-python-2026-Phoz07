#!/usr/bin/env python


def add_one(x):
    x += 1


number = 1

print(number)
add_one(number)
print(number)

# สิ่งที่สังเกตได้คือค่าของ number ไม่เปลี่ยนแปลงเพราะมันเป็นค่าที่ถูกส่งเข้าไปในฟังก์ชัน add_one แต่ไม่ได้เปลี่ยนแปลงค่าในตัวแปร number ที่อยู่นอกฟังก์ชัน