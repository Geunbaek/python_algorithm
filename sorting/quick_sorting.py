def quick_sorting(arr):
    if len(arr) <= 1:
        return arr
    left = []
    right = []
    pivot = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sorting(left) + [pivot] + quick_sorting(right)

arr = [1,9,8,6,5,4,3,2,7]
print(quick_sorting(arr))

import random
arr2 = random.sample(range(500), 10)
print(quick_sorting(arr2))
