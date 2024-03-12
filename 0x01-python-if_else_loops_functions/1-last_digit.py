#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit = number
if ldigit < 0:
    ldigit = -ldigit
    ldigit = ldigit % 10
    ldigit = -ldigit
else:
    ldigit = number % 10
if ldigit > 5:
    print(f"Last digit of {number:d} is {ldigit:d} and is greater than 5")
elif ldigit == 0:
    print(f"Last digit of {number:d} is {ldigit:d} and is 0")
elif ldigit < 6 and ldigit != 0:
    print(f"Last digit of {number} is {ldigit} and is less than 6 and not 0")
