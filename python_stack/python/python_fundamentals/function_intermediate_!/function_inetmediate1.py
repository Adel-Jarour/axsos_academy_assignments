import random

def randInt(min = 0, max = 100):
    if min > max:
        return False
    num = int(random.random() * (max - min + 1) + min)
    return num

print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))
