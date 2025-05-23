import random as ra

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    sort_left = merge_sort(left_arr)
    sort_right = merge_sort(right_arr)


    return merge(sort_left, sort_right)


def merge(left_arr, right_arr):
    arr_sorted = []
    while len(left_arr) > 0 and len(right_arr) > 0:
        if left_arr[0] > right_arr[0]:
            arr_sorted.append(right_arr[0])
            right_arr.pop(0)
        else:
            arr_sorted.append(left_arr[0])
            left_arr.pop(0)

    while len(left_arr) > 0:
        arr_sorted.append(left_arr[0])
        left_arr.pop(0)

    while len(right_arr) > 0:
        arr_sorted.append(right_arr[0])
        right_arr.pop(0)

    return arr_sorted


arr = [ra.randint(0,100) for i in range(10)]

arr_ordenado = merge_sort(arr)

print(arr_ordenado)