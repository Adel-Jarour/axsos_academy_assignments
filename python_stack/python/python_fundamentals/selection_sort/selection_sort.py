def selectionSort(lst):
    n = len(lst)
    
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        
        lst[i], lst[min_index] = lst[min_index], lst[i]
    
    return lst

print(selectionSort([8, 5, 2, 6, 4, 7, 0, 1, 3, 9]))