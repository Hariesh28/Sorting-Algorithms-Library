from ._utils import Heap

def heap_sort(array: list, ascending: bool = True) -> list:

    """
    Sorts a given list using the heap sort algorithm. The function uses a heap data structure to
    sort the array either in ascending or descending order based on the `ascending` parameter.

    Parameters:
        array (list[int]): The list of integers to be sorted.
        ascending (bool): A flag indicating the sort order. If True, the list will be sorted in
                          ascending order, otherwise in descending order. Default is True.

    Returns:
        list[int]: The sorted list.

    Examples:
        >>> heap_sort([4, 2, 7, 3, 1], ascending=True)
        [1, 2, 3, 4, 7]

        >>> heap_sort([4, 2, 7, 3, 1], ascending=False)
        [7, 4, 3, 2, 1]
    """

    is_max_heap = False if ascending else True

    heap = Heap(array, is_max_heap)

    return [heap.extract_root() for _ in range(heap.size)]
