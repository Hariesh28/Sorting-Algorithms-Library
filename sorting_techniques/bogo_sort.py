from random import shuffle
from ._utils import is_sorted

def bogo_sort(array: list, ascending: bool = True) -> list:

    """
    Sorts the given list using the Bogo Sort algorithm.

    Bogo Sort repeatedly shuffles the list until it is sorted in the specified order.
    This is a highly inefficient algorithm, only used for educational purposes or as a joke.

    Parameters:
        array (list): The list of elements to sort. Elements must be comparable.
        ascending (bool): If True, sorts in ascending order; if False, sorts in descending order.

    Returns:
        list: The sorted list.

    Example:
        >>> bogo_sort([3, 1, 2], ascending=True)
        [1, 2, 3]
        >>> bogo_sort([1, 2, 3], ascending=False)
        [3, 2, 1]
    """

    # Shuffle until sorted
    while not is_sorted(array, ascending=ascending):
        shuffle(array)

    return array
