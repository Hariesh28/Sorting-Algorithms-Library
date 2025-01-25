def counting_sort(array : list[int], ascending : bool = True) -> list[int]:

    """
    Sorts a given list using the Counting Sort algorithm. This algorithm uses a counting
    array to sort integers either in ascending or descending order based on the `ascending` parameter.

    Parameters:
        array (list[int]): The list of integers to be sorted.
        ascending (bool): A flag indicating the sort order. If True, the list will be sorted in
                          ascending order, otherwise in descending order. Default is True.

    Returns:
        list[int]: The sorted list.

    Raises:
        TypeError: If the array contains non-integer elements.

    Examples:
        >>> counting_sort([4, 2, 7, 3, 1], ascending=True)
        [1, 2, 3, 4, 7]

        >>> counting_sort([4, 2, 7, 3, 1], ascending=False)
        [7, 4, 3, 2, 1]

        >>> counting_sort([-3, 4, 2, 0, -1], ascending=True)
        [-3, -1, 0, 2, 4]
    """

    if not array:
        return []

    # Ensure all elements are integers
    if not all(isinstance(x, int) for x in array):
        raise TypeError("All elements in the array must be integers.")

    min_value = min(array)
    max_value = max(array)

    # Calculate the offset to map min number to index 0 in the `count` array
    offset = -min_value

    count = [0] * (max_value - min_value + 1)

    for value in array:
        count[value + offset] += 1

    result = []

    if ascending:
        for value, frequency in enumerate(count):
            result.extend([value - offset] * frequency)

    else:
        for i in range(len(count)-1, -1, -1):
            result.extend([i - offset] * count[i])

    return result
