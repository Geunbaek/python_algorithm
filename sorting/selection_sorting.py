def selection_sorting(arr):
    for index in range(len(arr)-1):
        min_index = index
        for index2 in range(index+1, len(arr)):
            if arr[min_index] > arr[index2]:
                min_index = index2
        arr[min_index], arr[index] = arr[index], arr[min_index]

    return arr

arr = [9,8,7,6,5,4,3,2,1]
print(selection_sorting(arr))