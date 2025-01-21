def quick_sort(array : list, ascending : bool = True) -> list:

    """
    Sorts the given list using the Quick Sort algorithm.

    Quick Sort is a divide-and-conquer algorithm that selects a pivot element, partitions the list into two sublists
    (elements less than the pivot and elements greater than or equal to the pivot), and recursively sorts the sublists.

    Parameters:
        array (list): The list of elements to sort. Elements must be comparable.

    Returns:
        list: The sorted list.

    Example:
        >>> quick_sort([3, 1, 2])
        [1, 2, 3]
        >>> quick_sort([5, 3, 8, 4, 2])
        [2, 3, 4, 5, 8]

    Notes:
        - This implementation uses the median-of-three strategy to select the pivot element for improved performance.
        - The function is not in-place and returns a new sorted list.
    """

    comparator_left = (lambda x, y: x < y) if ascending else (lambda x, y: x > y)
    comparator_right = (lambda x, y: x > y) if ascending else (lambda x, y: x < y)

    if len(array) <= 1:
        return array

    pivot = pivot_index(array)

    # Move the pivot element to the end of the array for easier partitioning.
    array[pivot], array[-1] = array[-1], array[pivot]

    left = 0
    right = len(array) - 2

    # Partition the array into elements less than and greater than the pivot.
    while left <= right:
        while comparator_left(array[left], array[-1]): left += 1
        while comparator_right(array[right], array[-1]): right -= 1

        if left < right:
            array[left], array[right] = array[right], array[left]

    # Place the pivot element in its correct position.
    array[left], array[-1] = array[-1], array[left]

    # Recursively sort the left and right partitions and combine the results.
    return quick_sort(array[:left], ascending) + [array[left]] + quick_sort(array[left+1:], ascending)


def pivot_index(array : list) -> int:

    """
    Determines the pivot index using the median-of-three strategy.

    The median-of-three strategy selects the pivot as the median value among the first, middle, and last elements of the list.
    This helps improve partitioning and reduces the likelihood of worst-case performance.

    Parameters:
        array (list): The list of elements for which the pivot index is to be determined.

    Returns:
        int: The index of the pivot element.

    Example:
        >>> pivot_index([8, 3, 5, 1])
        2
        >>> pivot_index([10, 7, 9, 6])
        1
    """

    low = 0
    high = len(array) - 1
    mid = len(array) // 2

    # Sort the first, middle, and last elements to find the median.
    if array[low] > array[mid]:
        low, mid = mid, low

    if array[low] > array[high]:
        low, high = high, low

    if array[mid] > array[high]:
        mid, high = high, mid

    return mid
