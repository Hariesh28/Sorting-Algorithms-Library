"""
Sorting Algorithms Library
--------------------------
This package provides efficient implementations of various sorting algorithms.
The goal is to provide clear, understandable, and educational implementations of
popular sorting algorithms, ideal for learning purposes and reference.

Standard Sorting Algorithms
---------------------------
- **Bubble Sort**: A simple sorting algorithm that repeatedly swaps adjacent elements if they are in the wrong order.
- **Selection Sort**: A simple comparison-based algorithm that repeatedly selects the smallest element.
- **Insertion Sort**: A simple comparison-based algorithm that builds the final sorted array one item at a time.
- **Merge Sort**: A divide-and-conquer algorithm that splits the array into smaller arrays, sorts them, and merges them.
- **Quick Sort**: A divide-and-conquer algorithm that picks a pivot element and partitions the array into two sub-arrays.
- **Heap Sort**: A comparison-based algorithm that uses a binary heap data structure.
- **Counting Sort**: A non-comparative sorting algorithm that sorts by counting the occurrences of each value.
- **LSD (Least Significant Digit) Radix Sort**: A non-comparative sorting algorithm that processes the digits of the numbers from least significant to most significant.

Fun Sorting Algorithms
----------------------
- **Bogo Sort**: A highly inefficient sorting algorithm based on random shuffling.

Documentation:
---------------
For detailed documentation and examples, visit:
    https://github.com/Hariesh28/Sorting-Algorithms-Library#readme

Usage Example:
--------------
    >>> from sorting_algorithms_library import merge_sort
    >>> merge_sort([5, 2, 9, 1, 5, 6])
    [1, 2, 5, 5, 6, 9]
"""

import logging
import webbrowser

__version__ = "1.0.5"
__author__ = "Hariesh R"
__status__ = "Production"
__python_requires__ = ">=3.9"
__license__ = "GPL-3.0"
__email__ = "hariesh28606@gmail.com"
__url__ = "https://github.com/Hariesh28/Sorting-Algorithms-Library"
__description__ = "A curated collection of sorting algorithm implementations with clear code and examples, ideal for learning and reference."

# Set up logging configuration
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Import sorting algorithm implementations
from ._utils import is_sorted
from .bogo_sort import bogo_sort
from .heap_sort import heap_sort
from .quick_sort import quick_sort
from .merge_sort import merge_sort
from .bubble_sort import bubble_sort
from .radix_sort_lsd import radix_sort
from .counting_sort import counting_sort
from .selection_sort import selection_sort
from .insertion_sort import insertion_sort
from ._utils import generate_random_numbers
from .radix_sort_lsd import counting_sort_digit_based

# Define the public API of the package
__all__ = [
    "is_sorted",
    "bogo_sort",
    "heap_sort",
    "merge_sort",
    "quick_sort",
    "radix_sort",
    "bubble_sort",
    "counting_sort",
    "insertion_sort",
    "selection_sort",
    "generate_random_numbers",
    "counting_sort_digit_based"
]

def get_version():
    """Return the current version of the package."""
    return __version__

def show_docs():
    """Open the documentation for this package in a web browser."""
    webbrowser.open(__url__)

def test():
    """Run a basic test to verify the package functionality."""
    test_array = [5, 3, 8, 4, 2]
    expected_result = sorted(test_array)
    result = merge_sort(test_array)

    if result == expected_result:
        logger.info("All tests passed successfully!")
    else:
        logger.error("Test failed: Merge Sort did not return the expected result.")
        raise AssertionError("Test failed: Merge Sort did not return the expected result.")

if __name__ == "__main__":
    raise ImportError("This is a package's __init__.py file, not a script. Import the package instead.")
