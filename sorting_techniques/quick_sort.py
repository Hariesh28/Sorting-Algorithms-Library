def quick_sort(array : list) -> list:

    if len(array) <= 1:
        return array

    pivot = pivot_index(array)
    array[pivot], array[-1] = array[-1], array[pivot]

    left = 0
    right = len(array) - 2

    while left <= right:
        while array[left] < array[-1]: left += 1
        while array[right] > array[-1]: right -= 1

        if left < right:
            array[left], array[right] = array[right], array[left]

    array[left], array[-1] = array[-1], array[left]

    return quick_sort(array[:left]) + [array[left]] + quick_sort(array[left+1:])

def pivot_index(array : list) -> int:

    low = 0
    high = len(array) - 1
    mid = len(array) // 2

    if array[low] > array[mid]:
        low, mid = mid, low

    if array[low] > array[high]:
        low, high = high, low

    if array[mid] > array[high]:
        mid, high = high, mid

    return mid
