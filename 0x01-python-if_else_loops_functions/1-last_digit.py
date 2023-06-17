#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
sign = ""
if number < 0:
    sign = "-"
if last > 5:
    print(f"Last digit of {number} is {sign}{last} and is greater than 5")
elif last == 0:
    print(f"Last digit of {number} is {sign}{last} and is 0")
elif last < 6 and last != 0:
    print(f"Last digit of {number} is {sign}{last} and is less than 6 and not 0")
