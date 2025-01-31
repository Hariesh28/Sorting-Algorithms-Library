def merge_sort(array : list, ascending : bool = True):

    """
    Sorts the given list using the Merge Sort algorithm.

    Merge Sort is a divide-and-conquer algorithm that recursively divides the list into halves, sorts each half, and then merges them back together in sorted order.

    Parameters:
        inputArray (list): The list of elements to sort. Elements must be comparable.
        ascending (bool): If True, sorts in ascending order; if False, sorts in descending order.

    Returns:
        list: The sorted list.

    Example:
        >>> merge_sort([3, 1, 2], ascending=True)
        [1, 2, 3]
        >>> merge_sort([1, 2, 3], ascending=False)
        [3, 2, 1]
    """

    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left_array = merge_sort(array[:mid], ascending=ascending)
    right_array = merge_sort(array[mid:], ascending=ascending)

    return merge(left_array, right_array, ascending=ascending)

def merge(array1 : list, array2 : list, ascending : bool = True):

    comparator = (lambda x, y: x <= y) if ascending else (lambda x, y: x >= y)

    left = right = 0
    merged_array = []

    while left < len(array1) and right < len(array2):

        if comparator(array1[left], array2[right]):
            merged_array.append(array1[left])
            left += 1

        else:
            merged_array.append(array2[right])
            right += 1

    merged_array.extend(array1[left:])
    merged_array.extend(array2[right:])

    return merged_array
