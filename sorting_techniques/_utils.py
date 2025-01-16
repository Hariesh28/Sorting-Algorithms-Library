def is_sorted(array: list | tuple, ascending: bool = True) -> bool:

    """
    Determines if the given array (list or tuple) is sorted in the specified order.

    Parameters:
        array (list | tuple): The sequence of elements to check. Elements must be comparable.
        ascending (bool): If True, checks for ascending order; if False, checks for descending order.

    Returns:
        bool: True if the array is sorted in the specified order, False otherwise.

    Examples:
        >>> is_sorted([1, 2, 3, 4], ascending=True)
        True
        >>> is_sorted((4, 3, 2, 1), ascending=False)
        True
        >>> is_sorted([3, 1, 2, 4], ascending=True)
        False
        >>> is_sorted([], ascending=True)
        True
    """

    if not array: return True

    comparator = (lambda x, y: x <= y) if ascending else (lambda x, y: x >= y)
    return all(comparator(array[i], array[i + 1]) for i in range(len(array) - 1))

def swap(inputArray: list[int], index1: int, index2: int) -> None:

    """
    Swaps the elements at the specified indices in the given list.

    Parameters:
        inputArray (list[int]): The list of integers in which the elements will be swapped.
        index1 (int): The index of the first element to swap.
        index2 (int): The index of the second element to swap.

    Returns:
        None: This function modifies the input list in place and does not return anything.

    Examples:
        >>> arr = [1, 2, 3, 4]
        >>> swap(arr, 0, 3)
        >>> arr
        [4, 2, 3, 1]

        >>> arr = [10, 20, 30, 40]
        >>> swap(arr, 1, 2)
        >>> arr
        [10, 30, 20, 40]
    """

    temp = inputArray[index1]
    inputArray[index1] = inputArray[index2]
    inputArray[index2] = temp
