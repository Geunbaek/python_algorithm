def bubble_sorting(arr):
    for index in range(len(arr) - 1):
        swap = False
        for index2 in range(len(arr) - index - 1):
            if arr[index2] > arr[index2 + 1]:
                arr[index2], arr[index2 + 1] = arr[index2 + 1], arr[index2]
                swap = True
        if not swap:
            break
    return arr

arr = [5,3,5,6,7,3,4,1,9,8]
print(bubble_sorting(arr))
