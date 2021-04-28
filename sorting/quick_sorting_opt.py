def quick_sorting_opt(arr, left, right):
    pivot = arr[(left+right)//2]
    left_idx = left
    right_idx = right

    while left_idx <= right_idx:
        while arr[left_idx] < pivot:
            left_idx += 1
        while arr[right_idx] > pivot:
            right_idx -= 1

        if left_idx <= right_idx:
            arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]
            left_idx += 1
            right_idx -= 1

    if left < right_idx:
        quick_sorting_opt(arr, left, right_idx)
    if right > left_idx:
        quick_sorting_opt(arr, left_idx, right)

import random

arr = random.sample(range(100), 10)
sorted_arr = sorted(arr)
quick_sorting_opt(arr, 0, len(arr)-1)
print(arr)
if sorted_arr == arr:
    print(True)



