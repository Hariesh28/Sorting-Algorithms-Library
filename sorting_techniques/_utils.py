from random import sample, choice

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

def generate_random_numbers(
    list_size : int = 10,
    range_start : int = 0,
    range_end : int = 20,
    repetition : bool = True,
    unique_count : int | None = None
) -> list[int]:

    """
    Generate a list of random numbers.

    Parameters:
    - list_size (int): Total number of elements in the list. Default is 10.
    - range_start (int): Minimum value of the numbers. Default is 0.
    - range_end (int): Maximum value of the numbers. Default is 20.
    - repetition (bool): Whether repetition is allowed in the list. Default is True.
    - unique_count (int): Number of unique numbers to use. If None, all numbers in the range are considered.

    Returns:
    - list[int]: A list of random numbers with possible repetition.

    Raises:
    - ValueError: If unique_count exceeds the possible range of unique numbers.
    """

    if list_size == 0 or unique_count == 0:
        return []

    if unique_count is None:
        unique_count = range_end - range_start + 1

    if unique_count > (range_end - range_start + 1):
        raise ValueError("unique_count exceeds the possible range of unique numbers.")

    # Generate the pool of unique numbers
    unique_numbers = sample(range(range_start, range_end+1), unique_count)

    if not repetition:
        if list_size > unique_count:
            raise ValueError("list_size cannot exceed unique_count when repetition is False.")

        return unique_numbers[:list_size]

    # Generate the random numbers with repetition
    return [choice(unique_numbers) for _ in range(list_size)]

class Heap:

    """
    A class representing a heap data structure. This can function as both a max-heap and a min-heap,
    depending on the `is_max_heap` flag passed during initialization. A max-heap is simulated by negating
    the values in the heap array.

    Attributes:
        array (list): The array representation of the heap.
        size (int): The current size of the heap.
        is_max_heap (bool): Flag indicating if the heap is a max-heap or min-heap.

    Methods:
        __init__(self, array, is_max_heap=False): Initializes the heap with the given array and heap type.
        _heapify(self, i): Ensures the heap property is maintained starting from index `i`.
        _build_heap(self): Builds the heap from the given array.
        extract_root(self): Removes and returns the root element (maximum for max-heap or minimum for min-heap).
    """

    def __init__(self, array, is_max_heap=False):

        """
        Initializes the heap with the given array. If `is_max_heap` is True, the heap will function as
        a max-heap; otherwise, it will function as a min-heap.

        Parameters:
            array (list[int]): The list of integers to be used as the initial heap.
            is_max_heap (bool): Flag indicating if the heap should be a max-heap or min-heap.

        Returns:
            None: The heap is initialized in place.
        """

        self.is_max_heap = is_max_heap
        self.size = len(array)

        # Invert the values for max-heap behavior
        if self.is_max_heap:
            self.array = [-x for x in array]

        else:
            self.array = array[:]

        self._build_heap()

    def _heapify(self, i):

        """
        Maintains the heap property by ensuring the element at index `i` is correctly placed according to the heap rules.
        It recursively swaps elements to maintain the heap structure.

        Parameters:
            i (int): The index of the element to be heapified.

        Returns:
            None: The heap is modified in place.
        """

        smallest = i  # Parent
        left = 2 * i + 1  # Left Child
        right = 2 * i + 2  # Right Child

        if left < self.size and self.array[left] < self.array[smallest]:
            smallest = left

        if right < self.size and self.array[right] < self.array[smallest]:
            smallest = right

        if smallest != i:
            swap(self.array, smallest, i)
            self._heapify(smallest)

    def _build_heap(self):

        """
        Builds the heap from the given array by calling `_heapify` on all non-leaf nodes in reverse order.

        Parameters:
            None: The method works on the internal heap array.

        Returns:
            None: The heap is modified in place.
        """

        # Start from the last non-leaf node and move in reverse
        for i in range(self.size // 2 - 1, -1, -1):
            self._heapify(i)

    def extract_root(self):

        """
        Removes and returns the root element from the heap. For a max-heap, this will return the maximum element;
        for a min-heap, this will return the minimum element.

        Parameters:
            None: The root element is removed from the heap.

        Returns:
            int or None: The root element of the heap, or None if the heap is empty.
        """

        if self.size > 0:
            root = self.array[0]
            self.array[0] = self.array[-1]
            self.array.pop()  # Remove the last element
            self.size -= 1
            self._heapify(0)

            # Return the negated root if it's a max-heap
            return -root if self.is_max_heap else root

        return None
