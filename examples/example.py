import os
import random
from sorting_techniques import (
    bogo_sort,
    heap_sort,
    merge_sort,
    quick_sort,
    radix_sort,
    bubble_sort,
    selection_sort,
    insertion_sort,
    counting_sort,
    generate_random_numbers
)

def clear_screen():
    """Clears the terminal screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("Choose a sorting algorithm to run:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    print("6. Heap Sort")
    print("7. Counting Sort")
    print("8. Radix Sort")
    print("9. Bogo Sort")
    print("10. Exit")

def main():
    clear_screen()

    while True:
        array = generate_random_numbers()

        display_menu()
        choice = input("Enter your choice (1-10): ").strip()

        ascending = random.choice([True, False])
        order_str = "ascending" if ascending else "descending"

        if choice == "1":
            print(f"Generated array: {array}")
            sorted_array = bubble_sort(array, ascending=ascending)
            print(f"Sorted array ({order_str}): {sorted_array}\n")

        elif choice == "2":
            print(f"Generated array: {array}")
            sorted_array = selection_sort(array, ascending=ascending)
            print(f"Sorted array ({order_str}): {sorted_array}\n")

        elif choice == "3":
            print(f"Generated array: {array}")
            sorted_array = insertion_sort(array, ascending=ascending)
            print(f"Sorted array ({order_str}): {sorted_array}\n")

        elif choice == "4":
            print(f"Generated array: {array}")
            sorted_array = merge_sort(array, ascending=ascending)
            print(f"Sorted array ({order_str}): {sorted_array}\n")

        elif choice == "5":
            print(f"Generated array: {array}")
            sorted_array = quick_sort(array, ascending=ascending)
            print(f"Sorted array ({order_str}): {sorted_array}\n")

        elif choice == "6":
            print(f"Generated array: {array}")
            sorted_array = heap_sort(array, ascending=ascending)
            print(f"Sorted array ({order_str}): {sorted_array}\n")

        elif choice == "7":
            print(f"Generated array: {array}")
            sorted_array = counting_sort(array, ascending=ascending)
            print(f"Sorted array ({order_str}): {sorted_array}\n")

        elif choice == "8":
            print(f"Generated array: {array}")
            sorted_array = radix_sort(array, ascending=ascending)
            print(f"Sorted array ({order_str}): {sorted_array}\n")

        elif choice == "9":
            print(f"Generated array: {array}")
            sorted_array = bogo_sort(array, ascending=ascending)
            print(f"Sorted array ({order_str}): {sorted_array}\n")

        elif choice == "10":
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")

        input("Press Enter to continue...\n")
        clear_screen()

if __name__ == "__main__":
    main()
