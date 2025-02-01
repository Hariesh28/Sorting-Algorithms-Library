def counting_sort_digit_based(array : list[int], exp : int = 0, ascending : bool = True) -> list[int]:

    """
    Sorts a list of integers based on the digit at a specified position (exponent)
    using the counting sort algorithm. This is a stable sorting method commonly
    used as a subroutine in Radix Sort.

    Parameters:
        array (list[int]): The list of integers to be sorted.
        exp (int): The exponent indicating the digit position to sort by
                   (e.g., for units place, exp=0; for tens place, exp=1; and so on).
        ascending (bool): If True, the array is sorted in ascending order;
                          if False, in descending order.

    Returns:
        list[int]: A new list where the input array is sorted based on the
                   specified digit position and order.

    Example:
        >>> counting_sort_digit_based([170, 45, 75, 90, 802, 24, 2, 66], exp=0, ascending=True)
        [802, 2, 24, 45, 66, 75, 170, 90]

        >>> counting_sort_digit_based([170, 45, 75, 90, 802, 24, 2, 66], exp=1, ascending=False)
        [75, 45, 66, 170, 90, 802, 2, 24]

    Notes:
        - The input list is not modified; the function returns a new sorted list.
        - Handles sorting by a single digit position, making it suitable for
          multi-pass sorting algorithms like Radix Sort.
        - The algorithm is stable, ensuring that the relative order of
          equal elements is preserved.

    Complexity:
        - Time Complexity: O(n + k), where n is the number of elements in the array
          and k is the range of digits (fixed at 10 for decimal digits).
        - Space Complexity: O(n + k), where k is the range of digits (10).
    """

    count = [0] * 10
    result = [0] * len(array)
    div = 10 ** exp

    # Count the occurrences of each digit at the current digit position
    for num in array:
        digit = num // div % 10
        count[digit] += 1

    # Update the count array to contain the cumulative count of digits
    if ascending:
        for i in range(1, 10):
            count[i] += count[i - 1]
    else:
        for i in range(8, -1, -1):
            count[i] += count[i + 1]

    # Build the result array in a stable manner, iterating from the end of the input array
    for i in range(len(array)-1, -1, -1):
        num = array[i]
        digit = num // div % 10
        count[digit] -= 1
        result[count[digit]] = num

    return result

def radix_sort(array : list[int], ascending : bool = True) -> list[int]:

    """
    Sorts a list of integers using the Radix Sort algorithm, handling both
    positive and negative numbers.

    Parameters:
        array (List[int]): The list of integers to be sorted.
        ascending (bool): If True, the array is sorted in ascending order;
                          if False, in descending order.

    Returns:
        List[int]: A new list containing the sorted integers in the specified order.

    Example:
        >>> radix_sort([170, -45, 75, -90, 802, 24, 2, -66], ascending=True)
        [-90, -66, -45, 2, 24, 75, 170, 802]

        >>> radix_sort([170, -45, 75, -90, 802, 24, 2, -66], ascending=False)
        [802, 170, 75, 24, 2, -45, -66, -90]

    Notes:
        - The algorithm separates positive and negative numbers for independent sorting.
        - Utilizes `counting_sort_digit_based` for stable sorting at each digit position.
        - The function is stable and preserves the relative order of equal elements.

    Complexity:
        - Time Complexity: O(n * d), where n is the number of elements and d is the max digit length.
        - Space Complexity: O(n + k), where k is the range of digits (10).

    Limitations:
        - Only works with integer inputs.
    """

    if not array:
        return []

    # Separate positive and negative numbers
    positive_numbers = [num for num in array if num >= 0]
    negative_numbers = [-num for num in array if num < 0]

    # Sort positive numbers
    if positive_numbers:
        positive_max_val = max(positive_numbers)

        exp = 0
        while positive_max_val // (10**exp) > 0:
            positive_numbers = counting_sort_digit_based(positive_numbers, exp, ascending)
            exp += 1

    # Sort negative numbers
    if negative_numbers:
        negative_max_val = max(negative_numbers)

        exp = 0
        while negative_max_val // (10**exp) > 0:
            negative_numbers = counting_sort_digit_based(negative_numbers, exp, not ascending)
            exp += 1

        # Convert back to negative
        negative_numbers = [-num for num in negative_numbers]

    # Combine results
    return negative_numbers + positive_numbers if ascending else positive_numbers + negative_numbers
