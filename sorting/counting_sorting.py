def counting_sorting(arr):
    _max = max(arr)
    counting_list = [0 for _ in range(_max+1)]
    result = []

    for elem in arr:
        counting_list[elem] += 1

    for num in range(len(counting_list)):
        for cnt in range(counting_list[num]):
            result.append(num)

    return result

arr = [9,4,1,123, 3,3, 789,7,9]
print(counting_sorting(arr))
