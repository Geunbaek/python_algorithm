def binary_search(sorted_list, search_data):
    if len(sorted_list) == 1 and sorted_list[0] == search_data:
        return True
    if len(sorted_list) == 1 and sorted_list[0] != search_data:
        return False
    if not sorted_list:
        return False

    mid = len(sorted_list) // 2

    if sorted_list[mid] < search_data:
        return binary_search(sorted_list[mid+1:], search_data)
    elif sorted_list[mid] > search_data:
        return binary_search(sorted_list[:mid], search_data)
    else:
        return True


import random

arr = random.sample(range(100), 10)
arr.sort()
print(arr)
print(binary_search(arr, 20))

