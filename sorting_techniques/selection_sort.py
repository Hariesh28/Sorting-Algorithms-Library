from ._utils import swap

def selection_sort(inputArray: list[int], ascending: bool = True) -> list[int]:

    """
    Sorts the given list using the Selection Sort algorithm.

    Selection Sort repeatedly selects the smallest (or largest) element from the unsorted portion of the list and swaps it with the element at the current position, gradually building the sorted list.

    Parameters:
        inputArray (list): The list of elements to sort. Elements must be comparable.
        ascending (bool): If True, sorts in ascending order; if False, sorts in descending order.

    Returns:
        list: The sorted list.

    Example:
        >>> selection_sort([3, 1, 2], ascending=True)
        [1, 2, 3]
        >>> selection_sort([1, 2, 3], ascending=False)
        [3, 2, 1]
    """


    length = len(inputArray)
    if(length==1): return inputArray
    outputArray = list(inputArray)
    for i in range(length):
        candidate = i
        for j in range(i,length):
            if ascending == (outputArray[candidate] > outputArray[j]):
                candidate = j
        swap(outputArray,i,candidate)
    return outputArray
