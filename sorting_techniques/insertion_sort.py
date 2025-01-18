from ._utils import swap

def insertion_sort(inputArray: list[int], ascending: bool = True) -> list[int]:

    """
    Sorts the given list using the Insertion Sort algorithm.

    Insertion Sort builds the final sorted array one element at a time by repeatedly shifting elements until they are in the correct order. It compares adjacent elements and swaps them if needed, continuing this process until the list is sorted.

    Parameters:
        inputArray (list): The list of elements to sort. Elements must be comparable.
        ascending (bool): If True, sorts in ascending order; if False, sorts in descending order.

    Returns:
        list: The sorted list.

    Example:
        >>> insertion_sort([3, 1, 2], ascending=True)
        [1, 2, 3]
        >>> insertion_sort([1, 2, 3], ascending=False)
        [3, 2, 1]
    """


    length = len(inputArray)
    if(length==1): return inputArray
    outputArray = list(inputArray)
    for i in range(1,length):
        for j in range(i,0,-1):
            if(ascending == (outputArray[j] > outputArray[j-1])):
                break
            swap(outputArray,j,j-1)
    return outputArray