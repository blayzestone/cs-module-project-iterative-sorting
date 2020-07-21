def linear_search(arr, target):
    for idx, val in enumerate(arr):
        if val == target:
            return idx

    return -1  # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    left_half = 0
    right_half = len(arr) - 1

    while left_half <= right_half:
        mid = (right_half + left_half) // 2

        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            right_half = mid - 1
        else:
            left_half = mid + 1

    return -1  # not found
