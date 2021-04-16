def merge_sorting(arr):

    def split_list(arr):
        if len(arr) <= 1:
            return arr

        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]

        return merge_list(split_list(left), split_list(right))

    def merge_list(left, right):
        merged = []
        left_index, right_index = 0, 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        while left_index < len(left):
            merged.append(left[left_index])
            left_index += 1

        while right_index < len(right):
            merged.append(right[right_index])
            right_index += 1

        return merged

    return split_list(arr)


import random

arr = random.sample(range(500), 10)
print(merge_sorting(arr))
if sorted(arr) == merge_sorting(arr):
    print(True)
else:
    print(False)


