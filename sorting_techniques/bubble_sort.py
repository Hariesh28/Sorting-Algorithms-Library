def bubble_sort(array : list[int], ascending : bool = True):

    """
    Sorts a given list using the Bubble Sort algorithm.

    Bubble Sort is a simple comparison-based sorting algorithm. It repeatedly steps
    through the list, compares adjacent elements, and swaps them if they are in the
    wrong order. The process continues until no more swaps are needed, indicating that
    the list is sorted.

    Parameters:
        array (List[int]): The list of integers to be sorted.
        ascending (bool): If True, sorts in ascending order; otherwise, sorts in descending order.

    Returns:
        List[int]: The sorted list of integers.

    Example:
        >>> bubble_sort([3, 1, 2])
        [1, 2, 3]
        >>> bubble_sort([5, 3, 8, 4, 2], ascending=False)
        [8, 5, 4, 3, 2]

    Notes:
        - This algorithm has a worst-case time complexity of O(n^2) where n is the number of elements in the list.
        - The function breaks early if the list becomes sorted before completing all iterations.
        - This implementation sorts the list in place and returns the sorted list.
    """

    comparator = (lambda x, y : x > y) if ascending else (lambda x, y : x < y)
    array = array.copy()

    if not array:
        return []

    for i in range(len(array)-1):

        swapped = False

        for j in range(len(array) - i - 1):
            if comparator(array[j], array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True

        # Break early if no swaps were made, indicating the list is sorted
        if not swapped:
            break

    return array
