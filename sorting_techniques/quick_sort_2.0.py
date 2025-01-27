import random

def quick_sort(array: list, ascending: bool = True) -> list:
    
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
    """
    
    if(len(array)<=1):
        return array
    pivot = array[random.randint(0,len(array)-1)]
    less = []
    mid = []
    more = []
    for i in array:
        if i < pivot:
            more.append(i)
            continue
        elif i > pivot:
            less.append(i)
            continue
        else:
            mid.append(i)
    if(ascending):
        return quick_sort(more,ascending=ascending) + mid + quick_sort(less,ascending=ascending)
    return quick_sort(less,ascending=ascending) + mid + quick_sort(more,ascending=ascending)
