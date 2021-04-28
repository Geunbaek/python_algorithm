def merge_sorting_opt(arr, left, right):
    if left == right:
        return
    mid = (left + right) // 2
    merge_sorting_opt(arr, left, mid)
    merge_sorting_opt(arr, mid+1, right)

    left_idx = left
    right_idx = mid + 1
    temp = []
    i = 0

    while left_idx <= mid and right_idx <= right:
        if arr[left_idx] <= arr[right_idx]:
            temp.append(arr[left_idx])
            left_idx += 1
        else:
            temp.append(arr[right_idx])
            right_idx += 1

    while left_idx <= mid:
        temp.append(arr[left_idx])
        left_idx += 1

    while right_idx <= right:
        temp.append(arr[right_idx])
        right_idx += 1

    for idx in range(left, right + 1):
        arr[idx] = temp[i]
        i += 1
    return

import random

arr = random.sample(range(100), 10)
sorted_arr = sorted(arr)
merge_sorting_opt(arr, 0, len(arr)-1)
print(arr)
if sorted_arr == arr:
    print(True)


