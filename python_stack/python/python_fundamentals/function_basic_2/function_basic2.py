def count_down(num):
    numbers = []
    for i in range(num, -1, -1):
        numbers.append(i)
    return numbers

print(count_down(5))

def print_and_return(list):
    print (list[0])
    return list[1]

print (print_and_return([1, 2]))

def first_plus_length(list):
    return (f"first value: {list[0]} + length: {len(list)}")

print(first_plus_length([1, 2, 3, 4, 5]))

def values_greater_than_second(list):
    if len(list) < 2:
        return False

    second = list[1]
    result = []

    for num in list:
        if num > second:
            result.append(num)

    print(len(result))
    return result

print (values_greater_than_second([5, 2, 3, 2, 1, 4]))

def length_and_value(size, value):
    return [value] * size

print (length_and_value(3, 4))