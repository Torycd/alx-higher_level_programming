#!/usr/bin/pyhton3
import random
number = random.randint(-10, 10)
if number > 0:
    print(number "is postive")
elif number == 0:
    print(number "is zero")
else:
    print(number "is negative")
