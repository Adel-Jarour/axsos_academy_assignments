def biggie_size (list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list

print("biggie size:", biggie_size([-1, 3, 5, -2, 0]))

def count_positive(list):
    sum = 0
    for i in list:
        if i > 0: 
            sum += 1

    list[len(list) - 1] = sum
    return list

print("count positive:", count_positive([-1, 1, 1, 1]))

def sum_total(list):
    sum = 0
    for i in list:
        sum += i
    
    return sum

print("sum total:", sum_total([1, 2, 3, 4]))

def average(list):
    sum = sum_total(list)
    return sum/len(list)

print("average:", average([1, 2, 3, 4]))

def length(list):
    len = 0
    for i in list:
        len += 1
    return len

print("length", length([37, 2, 1, 9]))

def minimum(list):
    if len(list) == 0:
        return False
    elif len(list) == 1:
        return list[0]
    
    mini = list[0]
    for i in range(1, len(list)):
        if list[i] < mini:
            mini = list[i]
    return mini

print("minimum:", minimum([37, 2, -1, -9]))

def maximum(list):
    if len(list) == 0:
        return False
    elif len(list) == 1:
        return list[0]
    
    max = list[0]
    for i in range(1, len(list)):
        if list[i] > max:
            max = list[i]
    return max

print("maximum:", maximum([37, 2, -1, -9]))

def ultimate_analysis(list):
    return {
        'sumTotlal': sum_total(list),
        'average': average(list),
        'minimum': minimum(list),
        'maximum': maximum(list),
        'length': length(list),
    }

print ('ultimate analysis:', ultimate_analysis([37, 2, -1, -9]))

def reverse_list(list):
    length = len(list)
    
    for i in range(length - 1, -1, -1):
        list.append(list[i])
    
    list = list[length:]
    return list

print ("reverse int:", reverse_list([37, 2, -1, -9]))

def reverse_list2(list):
    iteration = len(list) // 2

    for i in range(iteration):
        index_second_elem = len(list) - 1 - i
        temp = list[i]
        elem2 = list[index_second_elem]
        list[i] = elem2
        list[index_second_elem] = temp
    return list

print ("reverse int:", reverse_list2([37, 2, -1, -9]))
