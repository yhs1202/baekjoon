def bubble_sort(array, reverse=False):
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if not reverse:
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]  # swap
                    swapped = True
            else:
                if array[j] < array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]  # swap
        if not swapped:
            break  # No swaps means the array is sorted
    return array

num = int(input())
arr = []
for i in range(num):
    arr.append(int(input()))
    
arr_sort = bubble_sort(arr)
for element in arr_sort:
    print(element)