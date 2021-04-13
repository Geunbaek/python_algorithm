def insertion_sorting(arr):
    for index in range(len(arr)-1):
        for index2 in range(index+1, 0, -1):
            if arr[index2] < arr[index2-1]:
                arr[index2], arr[index2-1] = arr[index2-1], arr[index2]
            else:
                break

    return arr


arr = [1,9,8,6,5,4,3,2,7]
print(insertion_sorting(arr))