
print("Basic: ")
for i in range(151):
    print(i)

print("Multiples of Five: ")
for i in range(5, 1001, 5):
    print(i)

print("Counting, the Dojo Way: ")
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

sum = 0
for i in range(1, 500001, 2):
    sum += i

print("Whoa. That Sucker's Huge:", sum)

print("Countdown by Fours:")
for i in range(2018, 0, -4):
    print(i)

print("Flexible Counter:")
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)